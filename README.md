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
### Part 1 : Generating Twitter account keys

1. #### Create a Twitter account
To apply for Twitter developer key, you first of all need a Twitter account, if you do not have one, follow these steps to [create one](https://help.twitter.com/en/using-twitter/create-twitter-account)

2. #### Apply for Twitter developer key
The first thing I did was to apply for the Twitter developer key. This is not as straight forward as applying for the YouTube developer key. You're best chance is to apply as a hobbyist. This has a higher probability of your application getting approval. In some cases, it is instant, especially if your reason for applying is reasonable. Use [this link](https://developer.twitter.com/en/apply-for-access) to apply for access.

3. #### Keep your credentials private
When you finally get your credentials, its best to copy them and keep them safe.You will be presented with API_key, API_secret_key, Bearer_token, Access_token, and Access_token_secret. In writing the script, all will be needed but Bearer_token.

4. #### Set-up your environment.
The kind of environment to use is also key. There're a number of environments data engineers can deploy for this exercise. E.g, google colab, jupyter notebook, etc. I used jupyter notebook because I am conversant with it and also becuase all I do is saved on my local computer. For google colab, you'll need internet to create your workspace and to access your files. In situations where you have unstable internet, it delays execution of your project.

5.  #### Install the necessary packages 
By defualt, jyputer notebook doesn't come with pre-installed packages for interaction with Twitter backend. I had to install the Tweepy (pip install tweepy). Before installing these libraries, be sure to check your python version to aid installation of the appropriate client version. You can follow these [steps](https://www.toptal.com/python/twitter-data-mining-using-python) to help create an authentication object. 

6. #### define your own module
The next step I took was to hide my credentials by writing a script in my local container. I then imported the module in my script and call the credentials. There are others ways around but you have to find the way that best works for you.

supplementary files that helped me getaround the task
* [Twitter API doc](https://developer.twitter.com/en/docs/twitter-api/v1/tweets/search/api-reference/get-search-tweets)
* [Tweepy docs](http://docs.tweepy.org/en/latest/api.html)

### Part 2 Creating to MongoDB database
There are a number of ways to interact with mongo, using atlas,compass and also on out local machine. I had to work with my local machine so I installed mongodb using the terminal. 
1. #### Install Hombrew
I already had homebrew installed on my machine so it was pretty straight forward installing mongodb but if you do not have homebrew intalled, follow [these steps](https://docs.brew.sh/Installation) to install.

2. #### Install mongoDB locally
Follow these [steps](https://docs.mongodb.com/manual/tutorial/install-mongodb-on-os-x/) to install mongodb locally
3. #### Get started with Mongodb CRUD with python

Since I will be using python, I had to learn how to connect to mongo database. [Here](https://www.mongodb.com/blog/post/getting-started-with-python-and-mongodb) are the steps I followed to perform basic Create, Retreive, Update, and Delete (CRUD) operations using PyMongo

4. #### Caveats
I run into a problem when I was connecting to atlas which I want to point out. When you're experience ConnectionError, it can be an indication that PyMongo is not getting access to your database in Atlas. When this happens check the Database Access settings under Security and modify the authentcation method to SCRAM and MongoDB Roles to **readWriteAnyDatabase**@admin as shown in the image below
[logo][Users/Joshua/Joshua/Desktop/Scram.png]
