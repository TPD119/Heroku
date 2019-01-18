
# coding: utf-8

# ### Instructions
# 
# * Create a function that gets the weather in Washington, D.C. and Tweets it
# 
#   * Construct a Query URL for the OpenWeatherMap
# 
#   * Perform the API call to get the weather
# 
#   * Set up your Twitter credentials
# 
#   * Tweet the weather
# 
#   * Print the success message 
# 
#   * Set timer to run every 1 minute (for your Heroku app)

# In[ ]:


# Dependencies
import os
import tweepy
import time
import json
import random
import requests as req
import datetime


# In[ ]:


# Import Twitter and Weather API Keys

## COMMENT THIS OUT before deploying to Heroku!
#import sys
#sys.path.append('../../../../..')
#from config import consumer_key, consumer_secret, access_token, access_token_secret
#weather_api_key = "25bc90a1196e6f153eece0bc0b0fc9eb"

## REMOVE THESE COMMENTS before deploying to Heroku!
consumer_key = os.environ.get("consumer_key")
consumer_secret = os.environ.get("consumer_secret")
access_token = os.environ.get("access_token")
access_token_secret = os.environ.get("access_token_secret")
weather_api_key = os.environ.get("weather_api_key")


# In[ ]:


# Create a function that gets the weather in Washington, DC and Tweets it
def WeatherTweet():

    # Construct a Query URL for the OpenWeatherMap
    url = "http://api.openweathermap.org/data/2.5/weather?"
    city = "Washington, D.C."
    units = "imperial"
    query_url = url + "appid=" + weather_api_key + "&q=" + city + "&units=" + units

    # Perform the API call to get the weather
    weather_response = req.get(query_url)
    weather_json = weather_response.json()
    print(weather_json)

    # Twitter credentials
    auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
    auth.set_access_token(access_token, access_token_secret)
    api = tweepy.API(auth, parser=tweepy.parsers.JSONParser())

    # Tweet the weather
    api.update_status(
        "Weather in Washington, DC at " +\
        (datetime.datetime.now().strftime("%I:%M %p") + " is " +\
         str(weather_json["main"]["temp"])+"F"))

    # Print success message
    print("Tweeted successfully!")


# In[ ]:


# Set timer to run every 1 minute (for testing a Twitter deployment)
# Once deployed and things are working, you may want to change this! Or turn off your app. 
while(True):
    WeatherTweet()
    time.sleep(60)


# ### Export this file to Python (.py)
# 
# In order to run this deploy this script to Heroku, you will need to export this as a Python script (.py)
# 
# * From the Jupyter Notebook menu bar, click **File**
# * Choose **Download as**
# * Select **Python (.py)**
# 
# #### Before exporting to Python, be sure to replace the variable references!
