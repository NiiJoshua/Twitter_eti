# Twitter Data extraction : Project overview

This project is to extract data from Twitter, store the data in a csv format in a particular file name. The second part is to create a Mongodb Databases called **Tweets_db** and store the extracted tweets into a collection named: **raw_tweets**.

## Task
### Part 1
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
 - Username
 +	Screenname
 + Location
 -	Friends count
 - Verification status
 +	Description
 +	Followers count

### Part 2
Create a MongoDB database called Tweets_db and store the extracted tweets into a 	collection named: raw_tweets.

## Code and resources used
+ **Python version** : 3.6
+ **Packages** : json, pandas, tweepy, mongo db
+ **OS** : macOS Catalina
+ **Exteral client packages** mongo Atlas, mongo Compass
+ **Web Framework**: virtualenv, requirements.txt

## Activities done
### Part 1
1. **Create a Twitter account**
To apply for Twitter developer key, you first of all need a Twitter account, if you do not have one, follow these steps to [create one](https://help.twitter.com/en/using-twitter/create-twitter-account)
2. **Apply for Twitter developer key**
The first thing I did was to apply for the Twitter developer key. This is not as straight forward as applying for the YouTube developer key. You're best chance is to apply as a hobbyist. This has a higher probability of your application getting approval. In some cases, it is instant, especially if your reason for applying is reasonable. Use [this link](https://developer.twitter.com/en/apply-for-access) to apply for access.
3. **Keep your credentials private**
When you finally get your credentials, its best to copy them and keep them safe.You will be presented with API_key, API_secret_key, Bearer_token, Access_token, and Access_token_secret. In writing the script, all will be needed but Bearer_token.
4. ### Set-up your environment.
The kind of environment to use is also key. There're a number of environments data engineers can deploy for this exercise. E.g, google colab, jupyter notebook, etc. I used jupyter notebook because I am conversant with it and also becuase all I do is saved on my local computer. For google colab, you'll need internet to creat your workspace and to access your files. In situations where you have unstable internet, it delays execution of your project.
