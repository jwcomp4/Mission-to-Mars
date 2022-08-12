# Importing dependencies

from flask import Flask, render_template, redirect, url_for
# using flask to render a template, redirect to another url, and create a url
from flask_pymongo import PyMongo
# using PyMongo to interact with Mongo database
import scraping
# using the scraping code, we will convert from Jupyter notebook to Python

# setting up flask

app = Flask(__name__)

# use flask_pymongo to set up mongo connection

app.config['MONGO_URI'] = 'mongodb://localhost:27017/mars_app'
# tells Python our app will connect to Mongo using a uniform resource identifier (URI)
# the second half is the URL used to connect to Mongo. Tells port (27017) and db (mars_app)

mongo = PyMongo(app)

# Setting up the homepage route:

@app.route('/')

def index():
    mars = mongo.db.mars.find_one()
    return render_template('index.html', mars=mars)
# this initial route tells Flask what to display when looking at the homepage (index.html)
# So, when we visit the web app's HTML page, we see the homepage.
# the mars variable w/i the index funciton uses PyMongo to find mars collection in database 
# the return tells Flask to use an HTML template using an index.html file
# mars = mars tells Python to use the mars collection in MongoDB
# create a new varible to hold the newly scraped data, ref. the scrape_all function in scrape.py


# Setting up scraping route

@app.route('/scrape')

def scrape():
    mars = mongo.db.mars
    mars_data = scraping.scrape_all()
    mars.update_one({}, {"$set":mars_data}, upsert=True)
    # this line inserts data if an identical record doesn't exist
    # upsert tells Mongo to create a new document if one doesn't exist.
    return redirect('/', code=302)
    # this navigates back to the index.

if __name__ == '__main__':
    app.run()