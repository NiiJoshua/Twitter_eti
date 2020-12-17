
import tweepy as tw
from tweepy import OAuthHandler
import pandas as pd
import keys as k 
import time

api_key = k.credentials['api_key']
api_secret_key = k.credentials['api_secret']
access_token = k.credentials['access_token']
access_token_secret = k.credentials['access_token_secret']

auth = OAuthHandler(api_key, api_secret_key)
auth.set_access_token(access_token, access_token_secret)
api = tw.API(auth, wait_on_rate_limit=True, wait_on_rate_limit_notify=True)

tweets = []
def tweets_query(api,text_query,count,max_requests):
    tweets = tw.Cursor(api.search, q=text_query, since='2020-01-01').items(count)
    #tweets
    tweets_list  = [[tweet.text, tweet.id, tweet.source, tweet.coordinates, tweet.retweet_count, tweet.favorite_count,
                tweet.user._json['name'],tweet.user._json['screen_name'], tweet.user._json['location'], tweet.user._json['friends_count'],
                tweet.user._json['verified'], tweet.user._json['description'], tweet.user._json['followers_count']] for tweet in tweets]
    
    tweets_df= pd.DataFrame(tweets_list, columns = ['tweet_text','tweet_id', 'tweet_source','coordinates','retweet_count','likes_count','Username', 'screen_name','location', 'friends_count','verification_status','description','followers_count'])
    

def save_csv(tweets_df):
    tweets_df.to_csv('{}-tweets.csv'.format(text_query), sep=',', index = False)
    current_time = time.localtime()
    time.strftime("%Y%m%d_%H%M%S", current_time)
        
    ct_string = time.strftime("%Y%m%d_%H%M%S", current_time)
    print(ct_string)
        
    file_name =f"tweets_downloaded_{ct_string}.csv"
    tweets_df.to_csv(file_name)
    
print('Successful.')    

text_query = 'Election headquarters'
count = 200
max_requests = 3

tweets_query(api,text_query,count, max_requests)



import pymongo
from pymongo import MongoClient
import csv


client = MongoClient('localhost', 27017)
db=client['test']
db


class MongoDB(object):
    
    def __init__(self, dBName=None, collectionName=None ):
        self.dBName = dBName
        self.collectionName = collectionName
        
        self.client = client
        self.DB = self.client[self.dBName]
        self.collection = self.DB[self.collectionName]
        
    def InsertData(self, path=None):
        """
        :param path: Path os csv file
        :return: None
        """
        f = open(path, 'r')
        df = pd.read_csv(f)
        data = df.to_dict('records')
        
        self.collection.insert_many(data)
        print("All data have been uploded to server...")
        
if __name__ =='__main__':
    
    mongodb = MongoDB(dBName = 'Tweets_db', collectionName = 'raw_tweets')
    mongodb.InsertData(path = 'tweets_downloaded_20201208-191638.csv')





