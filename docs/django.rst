
Introduction
==================




Django Database
-----------------

The database is structured as a star schema. The fact table contains prices per retailer per timestamp per product.
The unique identifier for this table is the combination of timestamp, retailer and product. In future, this schema is
easily expandable with new dim-tables containing information on e.g. the retailers. Here is the schema:

.. image:: ./images/database.png
  :width: 800





Django Web-App
------------------

The web app for now only contains two simple visuals:

#. A line chart showing the historical prices of an iPhone 12, for the 10 retailers with lowest price today

#. A scatter plot showing retailer rating on the x-axis and price in the y-axis

The visuals have been created using the following procedure:

#. Query the DB to get only the needed data for the visual

#. Load data into a pandas dataframe

#. Use matplotlib to create the graph

#. Use mpld3 to convert the graph into html
