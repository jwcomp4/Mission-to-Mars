# Importing Dependencies

from splinter import Browser
from bs4 import BeautifulSoup as soup
from webdriver_manager.chrome import ChromeDriverManager
import datetime as dt
import pandas as pd

def scrape_all():
    # Setting up Splinter

    executable_path = {'executable_path': ChromeDriverManager().install()}

    browser = Browser('chrome', **executable_path, headless=True)

    news_title, news_paragraph = mars_news(browser)

    # Run all scraping functions and store results in dictionary
    # This dictionary runs all functions
    # When create HTML template, create paths to dictionary's values, allows to present data in the template.
    # Add the date the code was last run.

    data = {
        "news_title":  news_title,
        "news_paragraph": news_paragraph,
        "featured_image": featured_image(browser),
        "facts": mars_facts(),
        "last_modified": dt.datetime.now(),
        "hemispheres": hemispheres(browser)
    }

    browser.quit()

    return data

# assigning the url and instructing browswer to visit that url
# Refactoring for functions

def mars_news(browser):
    url = 'https://redplanetscience.com'

    browser.visit(url)

    # optional delay for loading the page:

    browser.is_element_present_by_css('div.list_text', wait_time=1)

    # Now setting up the HTML parser:

    html = browser.html

    news_soup = soup(html, 'html.parser')

    # Adding try/except block for error handling
    try:

        side_elem = news_soup.select_one('div.list_text')

        # beginning scraping
        # Using .find onto the side_elem variable to look for the specific information within the info the variable holds.
        # Running this code returns the HTML containing the content and everything else nested within the <div />

        side_elem.find('div', class_='content_title')

        # Only want the title.
        # Use the parent element to find the first 'a' tag and save it as 'news_title'
        # the .get_text() function chained to .find() returns only the text and not the HTML tags or elements.

        news_title = side_elem.find('div', class_='content_title').get_text()

        news_p = side_elem.find('div', class_='article_teaser_body').get_text()
    
    except AttributeError:

        return None, None

    return news_title, news_p

   


# ### JPL Space Images Featured Images

# Visit the image Space Images Mars website

def featured_image(browser):
    url = 'https://spaceimages-mars.com/'

    browser.visit(url)

    # Finding and Clicking the full image button
    # Chaining indexing at the end of the code telling the browser to click the second button.

    full_image_elem = browser.find_by_tag('button')[1]

    full_image_elem.click()

    # Parsing the new page to continue scraping the full-size image URL.

    html = browser.html

    img_soup = soup(html, 'html.parser')

    try:
    # Finding the relative image URL

        img_url_rel = img_soup.find('img', class_='fancybox-image').get('src')

    except AttributeError:
        return None
    
    # Use the base URL to create an absolute URL. 


    img_url = f'https://spaceimages-mars.com/{img_url_rel}'

  
    return img_url

def mars_facts():
# Scraping the table from Mars facts

    try:

        df = pd.read_html('https://galaxyfacts-mars.com')[0]

    except BaseException:
        # BaseException is somewhat of a catchall. raised when any built-in exceptions are encountered
        # and it won't handle any user-defined exceptions.
        # using here because using Pandas' read_html(), can result in errors other than AttributeError
        return None

    df.columns=['Description', 'Mars', 'Earth']

    df.set_index('Description', inplace=True)

   

    return df.to_html()

def hemispheres(browser):
    url = 'https://astrogeology.usgs.gov/search/results?q=hemisphere+enhanced&k1=target&v1=Mars'

    browser.visit(url)

    html = browser.html

    mars_soup = soup(html, 'html.parser')

    hemisphere_image_urls = []

    counter = 0

    for h in mars_soup.find_all('h3')[:4]:
        
        hemispheres = {}

        mars_link = browser.find_by_css('h3')[counter]
        
        mars_link.click()
        
        html = browser.html
        
        hem_soup = soup(html, 'html.parser')
        
        jpeg = hem_soup.li.find("a").get("href")
        
        hemispheres["image_url"] = jpeg
        
        title = hem_soup.find('h2', class_='title').get_text()
        
        hemispheres["title"] = title
        
        if hemispheres not in hemisphere_image_urls:
            hemisphere_image_urls.append(hemispheres)
        
        
        browser.back()
        
        counter += 1

    return hemisphere_image_urls


if __name__ == "__main__":

    print(scrape_all())




