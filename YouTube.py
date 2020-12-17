

from apiclient.discovery import build
from apiclient.errors import HttpError
import pandas as pd
import time
import datetime
import warnings
warnings.filterwarnings("ignore")


import key as k
key = k.credentials['DEVELOPER_KEY']



YOUTUBE_API_SERVICE_NAME = "youtube"
YOUTUBE_API_VERSION = "v3"

def youtube_search(q, max_results=100,order=None, token=None, location=None, location_radius=None):

    youtube = build(YOUTUBE_API_SERVICE_NAME, YOUTUBE_API_VERSION,developerKey=key)

    search_response = youtube.search().list(
    q=q,
    type="video",
    pageToken=token,
    order = order,
    part="id,snippet", # Part signifies the different types of data you want 
    maxResults=max_results,
    location=location,
    locationRadius=location_radius,videoDuration = 'medium', publishedAfter = '2020-01-01T00:00:00Z').execute()

    title = []
    channelId = []
    channelTitle = []
    categoryId = []
    videoId = []
    viewCount = []
    likeCount = []
    dislikeCount = []
    commentCount = []
    favoriteCount = []
    category = []
    videos = []
    description = []
    thumbnail_url = []
    video_url = []
    publish_time = []
    
    for search_result in search_response.get("items", []):
        if search_result["id"]["kind"] == "youtube#video":

            title.append(search_result['snippet']['title']) 

            videoId.append(search_result['id']['videoId'])

            response = youtube.videos().list(
                part='statistics, snippet',
                id =search_result['id']['videoId']).execute()

            channelId.append(response['items'][0]['snippet']['channelId'])
            channelTitle.append(response['items'][0]['snippet']['channelTitle'])
            categoryId.append(response['items'][0]['snippet']['categoryId'])
            favoriteCount.append(response['items'][0]['statistics']['favoriteCount'])
            viewCount.append(response['items'][0]['statistics']['viewCount']) 
            description.append(response['items'][0]['snippet']['description'])
            thumbnail_url.append(response['items'][0]['snippet']['thumbnails']['default']['url'])
            publish_time.append(response['items'][0]['snippet']['publishedAt'])
            video_url.append("https://www.youtube.com/watch?v=" +'id')
            
        if'commentCount' in response['items'][0]['statistics'].keys():
            commentCount.append(response['items'][0]['statistics']['commentCount'])
        else:
            commentCount.append([])
        if 'likeCount' in response['items'][0]['statistics'].keys():
             likeCount.append(response['items'][0]['statistics']['likeCount'])
        else:
            likeCount.append([])
        if 'dislikeCount' in response['items'][0]['statistics'].keys():
            dislikeCount.append(response['items'][0]['statistics']['dislikeCount'])
        else:
            dislikeCount.append([])
       
 

    youtube_dict = {'videoId': videoId,'title': title,'Description':description,'thumbnail_url': thumbnail_url,'videoId':videoId,'viewCount':viewCount,'likeCount':likeCount,'dislikeCount':dislikeCount,'commentCount':commentCount, 'publish_time':publish_time, 'video_url':video_url}

    return youtube_dict

test = youtube_dict("endsars")

test = pd.DataFrame(data = test)


test.head()

# ### Store file in datetime format

import datetime


current_timestamp = time.strftime("%Y%m%d-%H%M%S")
file_name = current_timestamp+"youtube_data.csv"
test.to_csv(file_name, index = False)

print("File name is successfully saved as {0}".format(file_name))







