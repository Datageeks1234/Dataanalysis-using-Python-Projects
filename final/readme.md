# Hubway Data Analysis 

<img width="900" alt="untitled" src="https://cloud.githubusercontent.com/assets/25045759/25140509/9b4fe4d6-242e-11e7-8954-17c529616d10.png">

## Introduction
Boston’s bike share program, Hubway, has quickly become a convenient, affordable and fun way to navigate in the city. This bike share program have embraced the influx of big data collected by their bike/station technology, using the rich datasets for their own business insights as well as posting many of them to the public for any aspiring data enthusiast to analyze.

## Data Resource
Hubway - The <a href="http://hubwaydatachallenge.org/trip-history-data/">Hubway Trip History dataset</a> contains information on over 1M bike trips spanning from the program’s inception in 2011 to mid-2013.

## Analysis 

# General Ridership Pattern analysis
* Hubway datasets provided information related number of bikes rented and its Time stamp i.e Departure time and Arrival time.
* Using this data calculated the mean of number of bikes
* In this analysis general ridership pattern is obtained as shown below
* Compared Mean of number of bikes rented during WEEKDAY vs WEEKEND

## Observations
* We can clearly undrestand that during WEEEKDAYS Morning(11AM-1PM) and Evening(6PM-8PM) more number of bikes are rented
* On WEEKEND (2PM-6PM) more number of bikes are rented. Seems like more number of users are interested to ride during middle of the day 

## Input Parameters
Duration, Number of rides, Start time, end time

## Steps
* Using api key request the data from URl and generate data frame with required parameters
* Defien weekday and weekend dictonaries
* Set different timings of a day using groupby to get 24 hrs format representation on x axis with 1 hr time interval 
* Calculate the mean of number of bikes rented at that particular timing
* Plot two graphs for weekend and weekday to compare peak bike ride timings.
* Use seaborn barplot with Time on x-axis and mean of number of bikes of y-axis

## Output
### CSV Files: <a href="https://github.com/Uppalapa/Assignments/blob/master/final/data/analysis1.csv"/>General Ridership Pattern During Weekdays</a>
### Plot Files: <a href="https://github.com/Uppalapa/Assignments/blob/master/final/extra/analysis1.png"/>General Ridership Pattern During Weekdays plot</a>

### (Part-1) General Ridership Pattern During Weekdays
![analysis1](https://cloud.githubusercontent.com/assets/25045759/25202544/be8ab3e0-2523-11e7-980b-f9154b9300d0.png)

## Output
### CSV Files:<a href="https://github.com/Uppalapa/Assignments/blob/master/final/data/analysis1.csv"/>General Ridership Pattern During Weekend</a>
### Plot Files:<a href="https://github.com/Uppalapa/Assignments/blob/master/final/extra/analysis1_2.png"/>General Ridership Pattern During Weekend plot</a>

### (Part-2) General Ridership Pattern During Weekend
![analysis1_2](https://cloud.githubusercontent.com/assets/25045759/25202545/be8d3854-2523-11e7-9ee9-1e7b19eed072.png)


# Hubway bike seasonality analysis

* In this analysis we observed how the duaration of rides different based on seasons.
* Hubway datasets provided information starting from July-2011 to Nov-2013 according to the hubway data time stamps calculated the duration of rides 
* compared duration of rides for years 2011 and 2012 for different months
* For the year 2012 compared the duration of rides for January-June and July-December

## Observations

* There is seasonality, as it can be infered from part1 that bike usage is increased over years
* From part1 we can also infer that during starting of summer the duration of rides are high and in sever summer or winter seasons the duration of rides are very low
* From part2, For the year 2012 on an average the higest duration of ride lasted for 5.2hrs in the month of July
* For the year 2011 on an average the higest duration of ride lasted for 3.6hrs in the month of August
* From part3, we can notice how duration of riding hubway bikes increased by females when compared to year 2011 

### (Part-1) Comparision of duration of rides(2011-2012)
## Input Parameters
Duration, start time, end time
## Steps
* Using api key request the data from URl and generate data frame with required parameters
* Calculate the duration of rides for every month in both the years 2011 and 2012
* Plot the values using seaborn and matplotlib plot a line graph with month of the year on X-axis, Duration of rides on Y-axis 
## Output
### CSV Files:<a href="https://github.com/Uppalapa/Assignments/blob/master/final/data/analysis2_12011-01-01.csv"/>Duration of rides by year 2011</a>,<a href=" https://github.com/Uppalapa/Assignments/blob/master/final/data/analysis2_12012-01-01.csv"/>Duration of rides by year 2012
### Plot Files:<a href="https://github.com/Uppalapa/Assignments/blob/master/final/extra/analysis2.png"/> Duration of rides by year plot</a>

![analysis2](https://cloud.githubusercontent.com/assets/25045759/25202547/be8e8484-2523-11e7-9725-fc2934f37b12.png)

### (Part-2) Comparing Spring and Fall duration of rides
## Input Parameters
Duration, start time, end time
## Steps
* Using api key request the data from URl and generate data frame with required parameters
* Use group by function to group the months of both fall(july-dec) and spring(jan-june) seasons for the year 2012
* Plot the duration values using matplotlib pie chart for different months of a year
## Output
### CSV Files:<a href="https://github.com/Uppalapa/Assignments/blob/master/final/data/analysis2_12012-01-01.csv"/> Duration of rides by season for spring</a>, <a href="https://github.com/Uppalapa/Assignments/blob/master/final/data/analysis2_12012-07-01.csv"/> Duration of rides by season for fall</a>
### Plot Files:<a href="https://github.com/Uppalapa/Assignments/blob/master/final/extra/analysis2_1.png"/> Duration of rides by season plot</a>

<img width="500" height="550" alt="untitled" src=https://cloud.githubusercontent.com/assets/25045759/25202546/be8d5bcc-2523-11e7-8b32-683b6a234047.png>

### (Part-3) Duration of rides by Gneder for year 2011, 2012
## Input Parameters
Duration, start time, end time, gender
## Steps
* Using api key request the data from URl and generate data frame with required parameters
* Collect the required data for both the years 2011, 2012
* Count the gender with respect to duration data
* Plot the duration values using matplotlib plot group by Gender
## Output
### CSV Files:<a href="https://github.com/Uppalapa/Assignments/blob/master/final/data/analysis2_12011-01-01.csv "/> Duration of rides by Gender year 2011</a>, <a href="https://github.com/Uppalapa/Assignments/blob/master/final/data/analysis2_12012-01-01.csv "/> Duration of rides by Gender year 2012</a>
### Plot Files:<a href="https://github.com/Uppalapa/Assignments/blob/master/final/extra/analysis2_3.png" /> Duration of rides by Gender </a>

<img width="500" height="550" alt="untitled" src= https://cloud.githubusercontent.com/assets/25045759/25250597/39185ac0-25e4-11e7-807d-0cb59d32a0db.png >

# Riders Demographic analysis

* This analysis invovles riders demograph. 
* Analyzed which age group riders are more at which locations of massachusetts
* Also analysed rides distrubution according to different locations based on gender

## Observations
* From the first graph it can be infered that there are more number of riders in lunenberg(01462) of age group(30-40)
* Locations near to city there are more number of riders with age group less than 30
* In Suburbs there are more riders with age groups 40-50
* From the second graph we can clearly infer that there are more number of male riders than female riders

## Input Parameters
Bike number, Data of birth, Zip code

## Steps
* Using api key request the data from URl and generate data frame with required parameters
* Based on the date of birth calculate the age of riders
* Using count function calculate the number of bike rides
* Plot the values using matplotlib stacked bar plot with location zipcodes on X-axis, Number of rides on Y-axis group by Gender

## Output
### CSV Files:<a href="https://github.com/Uppalapa/Assignments/blob/master/final/data/analysis3.csv"/>Demographic analysis based on Age group</a>
### Plot Files:<a href="https://github.com/Uppalapa/Assignments/blob/master/final/extra/analysis3.png"/>Demographic analysis based on Age group Plot</a>

### (Part-1) Riders Demographic graph based on Age group
![analysis3](https://cloud.githubusercontent.com/assets/25045759/25202548/be910fec-2523-11e7-9bdf-1f86ff7d5ef5.png)

## Input Parameters
Bike number, Gender, Zip code

## Steps
* Using api key request the data from URl and generate data frame with required parameters
* Using count function calculate the number of bike rides
* Collect zip code details group by gender
* Plot the values using matplotlib stacked bar plot with location zipcodes on X-axis, Number of rides on Y-axis group by Riders Gender

## Output
### CSV Files:<a href="https://github.com/Uppalapa/Assignments/blob/master/final/data/analysis3.csv"/> Demographic analysis based on Gender</a>
### Plot Files:<a href="https://github.com/Uppalapa/Assignments/blob/master/final/extra/analysis3_1.png"/> Demographic analysis based on Gender Plot</a>
### (Part-2) Riders Demographic graph based on Gender
![analysis3_1](https://cloud.githubusercontent.com/assets/25045759/25202549/be923494-2523-11e7-9ea6-c6b046b7f3b1.png)

