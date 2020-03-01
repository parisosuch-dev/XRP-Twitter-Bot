"""
Author: Paris Osuch
Website: parisosuch.com
Date Created: Feb 13 2020
About: Twitter bot that tweets xrp analytic data every 30 minutes on the hour.
"""

## imports ##
import tweepy
import requests
import json
from datetime import datetime
import time


## Get Market Data From Nomics API ##
def getMarketData(apikey):
    """Gets market data from Nomics API
    parameters:
        apikey (string)
    return:
        returnData (list) - list of market data
    """
    url = "https://api.nomics.com/v1/currencies/ticker?key={}&ids=XRP&interval=1d,30d&convert=USD".format(apikey)
    response = requests.get(url)
    data = response.json()
    price = data[0]["price"]
    marketCap = data[0]["market_cap"]
    prcntChange = data[0]["1d"]["price_change_pct"]
    marketVolume = data[0]["1d"]["volume"]
    returnData = [price, marketCap, prcntChange, marketVolume]

    return returnData


## Twitter Authentication ##
def twitterAuth(consumerAPI, consumerSecretAPI, accessToken, accessSecretToken):
    """Authenticates bot and creates API object for tweeting
    parameters:
        consumerAPI (string)
        consumerSecretAPI (string)
        accessToken (string)
        accessSecretToken (string)
    return:
        tweepyAPI (object) - used in tweet() to tweet with API authenications
    """
    auth = tweepy.OAuthHandler(consumerAPI, consumerSecretAPI)

    auth.set_access_token(accessToken, accessSecretToken)

    tweepyAPI = tweepy.API(auth, wait_on_rate_limit=True, wait_on_rate_limit_notify=True)

    try:
        tweepyAPI.verify_credentials()
        print("Authentication OK")
    except:
        print("Error during Authentication")

    return tweepyAPI

## Time Check ##
def timeCheck():
    """Checks the time
    parameters:
        None
    return:
        time (list) - two integers representing minutes and seconds
    """
    minutes = datetime.now().minute
    seconds = datetime.now().second
    time = [minutes, seconds]

    return time

## System Time ##
def systemTime():
    """ the current system time in UTC
    parameters:
        None
    return:
        currentTime (string)
    """
    currentTime = datetime.now()

    return currentTime

## Tweet Check ##
def tweetCheck(minutes, seconds):
    """checks if the time is within the 15 min interval on the hour
    parameters:
        minutes (int)
        seconds (int)
    return:
        boolean value of True
    """
    if (minutes == 0 or minutes == 30) and (seconds == 0):
        return True

## Tweet ##
def tweet(tweepyAPI, marketData):
    """ the tweet
    parameters:
        tweepyAPI (object)
        marketData (list)
    return:
        None
    """
    price = marketData[0]
    price = float(price)
    price = round(price, 4)
    marketCap = marketData[1]
    prcntChange = marketData[2]
    marketVolume = marketData[3]
    tweet = "Current price of XRP is {}. 24hr Volume: {}.".format(price, marketVolume)

    tweepyAPI.update_status(tweet)

## Main ##
def main():

    ## Global Keys and Tokens ##

    # Nomic API key:
    marketAPIkey = "0bf678670377f0814e229eeefd93dc86"

    # Consumer API keys:
    consumerAPI = ""
    consumerSecretAPI = ""

    # Access Tokens:
    accessToken = ""
    accessSecretToken = ""

    # create tweepyAPI object
    tweepyAPI = twitterAuth(consumerAPI, consumerSecretAPI, accessToken, accessSecretToken)

     # while True, timeCheck()
    while True:
        currentTime = timeCheck()

        system = systemTime()
        print("System time: ",system)
        print("----")
        time.sleep(1)
        # check time to tweet
        minutes = currentTime[0]
        seconds = currentTime[1]
        greenLight = tweetCheck(minutes, seconds)

        # tweet if True
        if greenLight:

            # get market data
            marketData = getMarketData(marketAPIkey)

            # tweet
            print('Tweet Sent')
            tweet(tweepyAPI, marketData)

## Run Program ##
main()
