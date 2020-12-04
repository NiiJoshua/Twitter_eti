# Twitter_eti
Write a script that downloads tweets data on a specific search topic using the standard search API. The script should contain the following functions: 
1)	scrape_tweets() that has the following parameters:
a)	Search topic
b)	The number of tweets to download per request
c)	The number of requests
And returns a dataframe.
2)	Save_results_as_csv() that has the following parameters:
a)	the dataframe from the above function
And returns a csv file with the following naming format:
tweets_downloaded_yymmdd_hhmmss.csv (where ‘yymmdd_hhmmss’ is the current 	timestamp)      
The following attributes of the tweets should be extracted:
•	Tweet text
•	Tweet id
•	Source
•	Coordinates
•	Retweet count
•	Likes count
•	User info
  o	Username
  o	Screenname
  o	Location
  o	Friends count
  o	Verification status
  o	Description
  o	Followers count
