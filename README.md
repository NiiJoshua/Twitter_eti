# Twitter Data extraction : Project overview
---------------------------------------------
This project is to extract data from Twitter, store the data in a csv format in a particular file name. The second part is to create a Mongodb Databases called **Tweets_db** and store the extracted tweets into a collection named: **raw_tweets**.

## Task
Write a script that downloads tweets data on a specific search topic using the standard search API. The script should contain the following functions: 
1)	**scrape_tweets()** that has the following parameters:
*	Search topic
*	The number of tweets to download per request
*	The number of requests
And returns a dataframe.

2)	**Save_results_as_csv()** that has the following parameters:
*	the dataframe from the above function
And returns a csv file with the following naming format:
tweets_downloaded_yymmdd_hhmmss.csv (where ‘yymmdd_hhmmss’ is the current 	timestamp)     

The following attributes of the tweets should be extracted:
* Tweet text
* Tweet id
*	Source
*	Coordinates
*	Retweet count
*	Likes count
*	User info:
 ..* Username
 ..*	Screenname
 ..* Location
 ..*	Friends count
 ..*	Verification status
 ..*	Description
 ..*	Followers count

## Code and resources used
**Python version** : 3.6
**Packages** : json, pandas, tweepy, mongo db
**OS** : macOS Catalina
**Exteral client packages** mongo Atlas, mongo Compass
**Web Framework**: virtualenv, requirements.txt
