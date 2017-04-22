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
* During the WEEKEND (2PM-6PM) more number of bikes are rented

## Input Parameters

## Steps

## Output
### CSV Files: <a href="https://github.com/Uppalapa/Assignments/blob/master/final/data/analysis1.csv"/></a>
### Plot Files: <a href="https://github.com/Uppalapa/Assignments/blob/master/final/extra/analysis1.png"/></a>

First Header  | Second Header
------------- | -------------
Content Cell  | Content Cell
Content Cell  | Content Cell

### (Part-1) General Ridership Pattern During Weekdays
![analysis1](https://cloud.githubusercontent.com/assets/25045759/25202544/be8ab3e0-2523-11e7-980b-f9154b9300d0.png)

## Output
### CSV Files:<a href="https://github.com/Uppalapa/Assignments/blob/master/final/data/analysis1.csv"/></a>
### Plot Files:<a href="https://github.com/Uppalapa/Assignments/blob/master/final/extra/analysis1_2.png"/></a>

First Header  | Second Header
------------- | -------------
Content Cell  | Content Cell
Content Cell  | Content Cell


### (Part-2) General Ridership Pattern During Weekend
![analysis1_2](https://cloud.githubusercontent.com/assets/25045759/25202545/be8d3854-2523-11e7-9ee9-1e7b19eed072.png)


# Hubway bike seasonality analysis

* In this analysis we observed how the duaration of rides different based on seasons.
* Hubway datasets provided information starting from July-2011 to Nov-2013 according to the hubway data time stamps caluculated the duration of rides 
* compared duration of rides for years 2011 and 2012 for different months
* For the year 2012 compared the duration of rides for January-June and July-December

## Observations
* We can infer that during sever summer or winter seasons the duration of rides are very low
* For the year 2012 on an average the higest duration of ride lasted for 5.2hrs in the month of July
* For the year 2011 on an average the higest duration of ride lasted for 3.6hrs in the month of August

## Input Parameters

## Steps

## Output
### CSV Files:<a href=""/></a>
### Plot Files:<a href="https://github.com/Uppalapa/Assignments/blob/master/final/extra/analysis2.png"/></a>
First Header  | Second Header
------------- | -------------
Content Cell  | Content Cell
Content Cell  | Content Cell


### (Part-1)
![analysis2](https://cloud.githubusercontent.com/assets/25045759/25202547/be8e8484-2523-11e7-9725-fc2934f37b12.png)

## Input Parameters

## Steps

## Output
### CSV Files:<a href=""/></a>
### Plot Files:<a href="https://github.com/Uppalapa/Assignments/blob/master/final/extra/analysis2_1.png"/></a>
First Header  | Second Header
------------- | -------------
Content Cell  | Content Cell
Content Cell  | Content Cell


### (Part-2)
![analysis2_1](https://cloud.githubusercontent.com/assets/25045759/25202546/be8d5bcc-2523-11e7-8b32-683b6a234047.png)

## Input Parameters

## Steps

## Output
### CSV Files:<a href=""/></a>
### Plot Files:<a href="vhttps://github.com/Uppalapa/Assignments/blob/master/final/extra/analysis2_3.png"/></a>
First Header  | Second Header
------------- | -------------
Content Cell  | Content Cell
Content Cell  | Content Cell


### (Part-3)
![analysis2_3](https://cloud.githubusercontent.com/assets/25045759/25250597/39185ac0-25e4-11e7-807d-0cb59d32a0db.png)

## Input Parameters

## Steps

## Output
### CSV Files:<a href=""/></a>
### Plot Files:<a href=""/></a>
First Header  | Second Header
------------- | -------------
Content Cell  | Content Cell
Content Cell  | Content Cell
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

