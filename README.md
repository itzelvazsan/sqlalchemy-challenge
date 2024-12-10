# sqlalchemy-challenge

By: Itzel Vázquez Sánchez

## Project Description

This Week's Challenge had two parts:

:one: **First excercise: Part 1: Analyze and Explore the Climate Data**
In this part, with Python and SQLAlchemy we had to do a basic climate analysis and data exploration of a climate database. The activities are:
1. Use climate_starter.ipynb and hawaii.sqlite.
2. Use the SQLAlchemy create_engine() function to connect to your SQLite database.
3. Use the SQLAlchemy automap_base() function to reflect tables into classes, and then save references to the classes.
4. Link Python to the database by creating a SQLAlchemy session.
5. Perform a precipitation analysis and then a station analysis by completing the steps in the following two subsections.
    5.1. Precipitation Analysis: Find the most recent date in the dataset. Using that date, get the previous 12 months of precipitation     data by querying the previous 12 months of data. Select only the "date" and "prcp" values. Load the query results into a Pandas DataFrame. Explicitly set the column names. Sort the DataFrame values by "date". Finally, plot the results by using the DataFrame plot method. :memo: The plot should align with:

![image](https://github.com/user-attachments/assets/7eb390c4-433f-44fb-8c3a-5a0ed840323f)

  Use Pandas to print the summary statistics for the precipitation data.

  5.2. Station Analysis: Design a query to calculate the total number of stations in the dataset. Design a query to find the most-active stations (that is, the stations that have the most rows). Design a query that calculates the lowest, highest, and average temperatures that filters on the most-active station id found in the previous query. Design a query to get the previous 12 months of temperature observation (TOBS) data. Plot the results as a histogram with bins=12, as the following image:
![image](https://github.com/user-attachments/assets/cd0e6371-300e-4460-bd7c-b0c1daa40906)


 :two:**Second Excercise: Part 2: Design Your Climate App**
Design a Flask API based on the queries:

1. `/`
* Start at the homepage.
* List all the available routes.

2. `/api/v1.0/precipitation`
* Convert the query results from your precipitation analysis (i.e. retrieve only the last 12 months of data) to a dictionary using date as the key and prcp as the value.
* Return the JSON representation of your dictionary.

3. `/api/v1.0/stations`
* Return a JSON list of stations from the dataset.

4. `/api/v1.0/tobs`

* Query the dates and temperature observations of the most-active station for the previous year of data.
* Return a JSON list of temperature observations for the previous year.

5. `/api/v1.0/<start>` and `/api/v1.0/<start>/<end>`

* Return a JSON list of the minimum temperature, the average temperature, and the maximum temperature for a specified start or start-end range.
* For a specified start, calculate TMIN, TAVG, and TMAX for all the dates greater than or equal to the start date.
* For a specified start date and end date, calculate TMIN, TAVG, and TMAX for the dates from the start date to the end date, inclusive.


🤓 This Project is the result of the learning lessons of Module 10: Advanced SQL from the Data Analysis and Visualization Boot Camp 2024. The main goal is to use the acquired habilities and knowledge in a real case. 


## Table of contents

On the repository you can find two folders:

:one: **Folder 1: SurfsUp**
| Item  |   File Type   |         File Name              |           Description                      |
| ----- | ------------- | ------------------------------ | ------------------------------------------ |
|   1   |       .py     |           app.py               |  Script for a Flask API                    |
|   2   |     .ipynb    |  climate_starter               | Contains the results in a Jupyter Notebook |
|   3   |   folder      |          Resources             | Contains database in sqlite                |


## How to Use the Project
 
 * To solve the first problem: you can download the jupyter notebook file aling with the Resources folder. The code should run if you save the folders in the same directory as the script.
 
 * To solve the second problem: you can download the app.py file, and run it. 

## Credits
The code of this project origins from: starter code provided by the Team of the Data Analysis and Visualization Boot Camp, the excercises worked in the Zoom Lessons and the Solved versions of the code. I also used help from Stackoverflow, [Python Documentation](https://docs.python.org/3/), [SQLAlchemy Documentation](https://docs.sqlalchemy.org/en/20/) and Microsoft Copilot.

