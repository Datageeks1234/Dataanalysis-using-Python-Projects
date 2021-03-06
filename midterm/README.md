# DATA ANALYSIS USING PYTHON MIDTERM
###### Question-1
## ENRON SCANDAL DATASET
Tried focusing on following words during analysis:
Fraud,
Shutdown,
Bankcrupt/Bankcrupcy,
Litigation,
Cheat,
Sunk.

There are high chances that these words would be used somewhere. Tried to find the number of appearances of these words group by date and group by name. plotting the appearances by date would give rise and fall pattern of such words used this would give the idea about the sentiments (sentiment analysis) prevailing at different point of time. Also, the group by names would give an idea about important personalities involved in this.

Also, tried to make three - four topic groups of words, like,

Topic1: Business Legalities words: enron, deal, agreement, contract
Topic2: Business group related: gas, power etc
Topic3: Notices related to meetings: email, attach, thank, file, inform

These topics related grouped words are to be plotted date-wise to see a pattern this will give an idea about how and when different stages of discussion have prevailed.
## Analysis-1
Aim of analysis 1 is to find the Frequent Email exchanger: 

Mainly this analysis concentrates on finding the key player in fraud.

As a result of this analysis suspicious emails are dumped into email.text file and saved.

Also printing the suspecious mail ids and their respective frequencies.

Represented all the mail ids and their frequencies using matplotlib

![p1f](https://cloud.githubusercontent.com/assets/25045759/24582830/4c961d90-1706-11e7-8b00-f0298743e557.png)
<img width="600" height="600" alt="qe1 2" src="https://cloud.githubusercontent.com/assets/25045759/24969873/44e49496-1f80-11e7-9721-58237340a3a4.png">

## Analysis-2
Aim of analysis 2 is to Look through the pattern and to find, read and print 100 most common Keywords used during email exchanges

![p2f](https://cloud.githubusercontent.com/assets/25045759/24582832/4c9713ee-1706-11e7-8b0b-e92c77372063.png)

## Analysis-3
Aim of analysis 3 is to Spike in email exchange the time of bankcrupcy and print those email ids and contents

![p3f](https://cloud.githubusercontent.com/assets/25045759/24582831/4c9625ec-1706-11e7-8b9a-bb90b3fe01c7.png)


## NYT DATASET
###### Question-2

## Analysis-1

(part-1)
Analyzed Sports data from 2010-2017 and represented different percentage of sports categories using matplot lib pie chart.

<img width="381" alt="a2q1" src="https://cloud.githubusercontent.com/assets/25045759/25024774/4722728a-206d-11e7-81f2-d7ecf3ec3749.png">

(part-2)
Analyzed sports data for each year from 2010 - 2017 and saved the data in respective csv files.

Percentages of sports categories published in NYT for every year is represented using matplotlib pie charts 

<img width="750" height="400" alt="sportpie" src="https://cloud.githubusercontent.com/assets/25045759/25066180/6161ea8c-21ed-11e7-9056-1e43fd35c0e7.png">



## Analysis-2

(part-1)
Analyzed top 10 words and frequencies in the politics category and represented them using bar graphs

![politics](https://cloud.githubusercontent.com/assets/25045759/24582671/6f681872-1702-11e7-954d-f49ddbdaf5a6.png)

(part-2)
Analyzed the keyword for Hilary Clinton versus trump at the time of election 

found that Trump word frequency is greater than Hilary

Total number of words donald trump appeared in 2017 January is 11 and Hilary is 5

Plotted results using matplotlib

![politic](https://cloud.githubusercontent.com/assets/25045759/25052539/59e3ca46-2120-11e7-9b30-89aa7ce54d2e.png)


## Analysis-3
By considering 2014 December Articles we are finding the top Titles that appeared in NYT according to their frequency 

Plotted results using matplotlib

![toptilesanalysis](https://cloud.githubusercontent.com/assets/25045759/24582666/466190f2-1702-11e7-8565-20690162336b.png)
