# Importing Dependencies

from splinter import Browser
from bs4 import BeautifulSoup as soup
from webdriver_manager.chrome import ChromeDriverManager

import pandas as pd

# Setting up Splinter

executable_path = {'executable_path': ChromeDriverManager().install()}

browser = Browser('chrome', **executable_path, headless=False)

# assigning the url and instructing browswer to visit that url

url = 'https://redplanetscience.com'

browser.visit(url)

# optional delay for loading the page:

browser.is_element_present_by_css('div.list_text', wait_time=1)

# Now setting up the HTML parser:

html = browser.html

news_soup = soup(html, 'html.parser')

side_elem = news_soup.select_one('div.list_text')



# beginning scraping
# Using .find onto the side_elem variable to look for the specific information within the info the variable holds.
# Running this code returns the HTML containing the content and everything else nested within the <div />

side_elem.find('div', class_='content_title')

# Only want the title.
# Use the parent element to find the first 'a' tag and save it as 'news_title'
# the .get_text() function chained to .find() returns only the text and not the HTML tags or elements.

news_title = side_elem.find('div', class_='content_title').get_text()

news_title


news_p = side_elem.find('div', class_='article_teaser_body').get_text()

news_p


# ### JPL Space Images Featured Images

# Visit the image Space Images Mars website

url = 'https://spaceimages-mars.com/'

browser.visit(url)

# Finding and Clicking the full image button
# Chaining indexing at the end of the code telling the browser to click the second button.

full_image_elem = browser.find_by_tag('button')[1]

full_image_elem.click()

# Parsing the new page to continue scraping the full-size image URL.

html = browser.html

img_soup = soup(html, 'html.parser')

# Finding the relative image URL

img_url_rel = img_soup.find('img', class_='fancybox-image').get('src')

img_url_rel

# Use the base URL to create an absolute URL. 


img_url = f'https://spaceimages-mars.com/{img_url_rel}'

img_url

# Scraping the table from Mars facts

df = pd.read_html('https://galaxyfacts-mars.com')[0]

df.columns=['description', 'Mars', 'Earth']

df.set_index('description', inplace=True)

df

df.to_html()

browser.quit()





