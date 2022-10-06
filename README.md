# Mission to Mars: Web Scraping, MongoDB, and Flask

## Overview

- This challenge integrates skills from Python, HTML, CSS, Flask, and MongoDB to scrape data from the web, store it into a database, and then use that data to populate a new webpage focused on the following:
    - The latest Mars news
    - A table of basic Mars facts
    - A new photo of Mars from the Jet Propulsion Laboratory
    - Full resolution images of Mars hemispheres. 

## Challenges within the Analysis

- Deliverable 1: Creating for loop to capture high resolution images
    - Creating this for loop required the following: 
        1. Using DevTools to locate the germane data within the HTML
        2. Write Python using Splinter and BeautifulSoup to capture that data
        3. Loop through the webpage to capature the Title of each image and the corresponding URL
        4. Populate a dictionary and list with the scraped data.
- Deliverable 2: Update the Web App with the newly scraped images and titles
    - The main challenge here was updating the app.py file and index.html such that all 3 files communicated together to produce the desired end result. 
    - Employing indentation in the index.html file made for easier to read code and easier implementation.

## Summary

- This challenge nicely integrates several skills to build a functioning website with visual appeal. 
- The possibilities for this sort of skillset are quite wide.
