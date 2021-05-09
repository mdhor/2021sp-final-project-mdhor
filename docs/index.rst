.. Final Project, CSCI E-29 documentation master file, created by
   sphinx-quickstart on Wed Apr 28 18:13:52 2021.
   You can adapt this file completely to your liking, but it should at least
   contain the root `toctree` directive.

Welcome to Final Project, CSCI E-29's documentation!
====================================================================


----------------------------------

Introduction
============

Pricing and assortment data is highly valuable but can be difficult and expensive to obtain, especially for smaller retailers.

Because of digitalization, the importance of pricing and assortment data has increased. An insight into a companys online presence is crucial for success.
This is especially true after COVID-19, where smaller retailers are forced to differentiate themselves online.
Without large IT-budgets, gaining good data surrounding ones own as well as competitors pricing and assortment can be difficult.

Data on pricing and assortment can be used for several insightful analyses. One example is pricing analysis to answer questions like "Where do our prices differ from competitors?".
Another example is assortment analysis; "How does our assortment compare to competitors?".

prisjakt.no is a leading actor within price comparison in Norway. It acts as an "all-inclusive" shopping mall, so the consumer does not have to browse many different website, by comparing pricing
from many different retailers. Th products range widely from electronics to clothing to vehicles.

-------------------------------------

Quick-Start
============

If you want to test the project quickly, do the following:

1. Create an environment using the Pipfile
2. pipenv run python manage.py migrate
3. pipenv run python -m final_project
4. pipenv run python manage.py runserver
5. Enter the server and check out a visual

-------------------------------------


Aim of Project
==============

The project aims to create a full stack data science pipeline, from mining prisjakt.no data all the way to showing results in a web application.
The project can be split into four main workflows:

* Developing pj-scraper, a library that will act as a simplified interface for scraping of prisjakt.no
* Organizing the pipeline into Luigi Tasks, for organizing the workflow all the way from handling scraping to appending data in a Django database
* Creating a Django database that will contain the historical data that has been scraped from prisjakt.no
* Developing a simple Django web app to show a simple example of how the data can be used for analysis


High-Level Workflow
===================

.. image:: ./images/workflow.png
  :width: 800



-------------------------------------

pj-scraper
==========

The pj-scraper library is centered around the use of a single class, with methods that handle to main tasks:

* Getting all products from a category, e.g. all from the category "smartphones"
* Getting all retailers and prices for a product, e.g. all from the product "iPhone 12"



.. autoclass:: pj_scraper.scraper.Scraper
   :members:
   :undoc-members:
   :show-inheritance:

-------------------------------------

Luigi Workflow
==============

The workflow consists of four main tasks:

* Scrape products from a list of categories
* Scrape retailers and prices for all products
* Append any new products to database
* Append all prices to the database with a new timestamp


.. automodule:: final_project.tasks
   :members:
   :undoc-members:
   :show-inheritance:

-------------------------------------

Django Database
===============

Not yet added to docs

-------------------------------------

Django Web-App
==============

Not yet added to docs



-------------------------------------

Conclusion and Main Learnings
==============================

* Developing pj-scraper
   * The libraries requests and BeautifulSoup4 has been used to mine unstructured data from prisjakt.no
   * Two main functions have been developed: Getting all products from a category and getting all retailers and prices for a product or list of products
   * The tools sdist and Twine has been used to publish pj-scraper to PyPi for easy installation
* Organizing the workflow into Luigi Tasks
   * Four main tasks has been developed that encapsulates the full data science pipeline
   * The first two tasks handles the scraping of products, retailers and prices, utilizing the pj-scraper library
   * The last two tasks handles appending the scraped data to the Django database, using Django commands
* Creating a Django database
   * A Django database has been developed which contains two tables: Products and Prices
   * The Prices table is a fact table containing prices for each product and retailer for a given timestamp
   * The Products table is a dim-table containing information about products, like product name and category
* Developing a simple Django web app
   * A simple web app has been developed using the chartjs
   * To avoid unneseccary boilerplate and simplify visuals creation, django-chartjs has been used
   * A simple visual has been made, that shows ..........
