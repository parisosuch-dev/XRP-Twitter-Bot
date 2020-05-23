"""
/ main.py
-----------------------------
/ author: paris osuch
/ website: parisosuch.com
/ git-hub repo: https://github.com/parisosuch-dev/
-----------------------------
/ about: this program utilizes the pandas and matplotlib library to create a twitter bot
that updates the follower on market price action while providing a graph. Because there are no APIs
that grant full access to a non-commercial personel, I used pandas to handle and store the incoming data
in a csv file in the local directory.
NOTE: you will need create two folders inside the path called "data" and and "graph"
-----------------------------
"""
# / Imports
from timekeep import *
from twitterbot import *
from datahandler import *
from graph import Graph
import time

# / Main
def main():
    CAPI = 'nope'
    CSECRET = 'nope'
    TOKEN = 'nope'
    STOKEN = 'nope'
    FILEPATH = 'data\\data.csv'
    IMAGEPATH = 'graph\\graph.png'
    MARKETKEY = "nope"
    while True:
        # / /  create time object
        t = TimeKeep()
        sysTime = t.systemTime()
        print(f'> system time: {sysTime}')
        print('---------------------------')
        time.sleep(0.5)
        # / / create data handle object
        dh = DataHandle(MARKETKEY)
        # / / create twitter bot object
        bot = TwitterBot(CAPI, CSECRET, TOKEN, STOKEN)
        # / / get time date from TimeKeep.timeData
        tData = t.timeData()
        secs = tData[0]
        mins = tData[1]
        # / / create tweet times
        tweetMin = 0
        tweetSec = 0
        # / / if the time is right:
        greenLight = bot.tweetCheck(secs, mins, tweetMin, tweetSec)
        if greenLight is True:
            # / / if you have a full file (168 rows):
            length = dh.dataLen(FILEPATH)
            if length != 168:
                # / / get price data
                price = dh.marketPrice()
                # / / write data to file
                dh.dataWrite(FILEPATH)
                # / / delete first row
                dh.dataDel(FILEPATH, 0)
                # / / create graph and image
                g = Graph(FILEPATH, IMAGEPATH, MARKETKEY)
                # / / if current graph exists, delete the image of the graph
                g.delGraph()
                g.graphCreate()
                # / / create twitter object with TwitterBot.twitter()
                twitApi = bot.twitter()
                # / / tweet price and graph
                bot.tweet(twitApi, price, image = IMAGEPATH)
            # / / else: (not a full file)
            else:
                # / / get price data
                price = dh.marketPrice()
                # / / write data to file
                dh.dataWrite(FILEPATH)
                # / / create twitter object with TwitterBot.twitter()
                twitApi = bot.twitter()
                # / / tweet the price
                bot.tweet(twitApi, price)

main()