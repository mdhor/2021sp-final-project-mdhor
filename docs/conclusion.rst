
Conclusion and Main Learnings
==============================

#.  Developing pj-scraper

     *  The libraries requests and BeautifulSoup4 has been used to mine unstructured data from prisjakt.no

     *  Two main functions have been developed: Getting all products from a category and getting all retailers and prices for a product or list of products

     *  The tools sdist and Twine has been used to publish pj-scraper to PyPi for easy installation

#.  Organizing the workflow into Luigi Tasks

      *  Four main tasks has been developed that encapsulates the full data science pipeline

      *  The first two tasks handles the scraping of products, retailers and prices, utilizing the pj-scraper library

      *  The last two tasks handles appending the scraped data to the Django database, using Django commands

#.  Creating a Django database

      *  A Django database has been developed which contains two tables: Products and Prices
      *  The Prices table is a fact table containing prices for each product and retailer for a given timestamp
      *  The Products table is a dim-table containing information about products, like product name and category

#.  Developing a simple Django web app

      *  A simple web app has been developed, to showcase how the system could be used in practice

      *  To avoid unneseccary boilerplate and simplify visuals creation, mpld3 has been used

      *  Two simple visuals has been made, that shows two interesting analyses




Future Work
-------------------------------------

Before this project would have real value, two main things are missing:

#.  Move the system to the cloud and schedule Luigi to run with certain intervals

#.  Create insightful analyses based on inputs from potential users of the system
