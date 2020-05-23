"""
twitterbot.py
-----------------------------
/ author: paris osuch
/ website: parisosuch.com
/ git-hub repo: https://github.com/parisosuch-dev/
-----------------------------
/ about: utilizes the tweepy module in order to create a twitter api
and twitter bot to be used in main.py
-----------------------------
/ twitterBot class:
/ / twitter() method
/ / tweetCheck() method
/ / tweet() method
"""
# -- Imports
import tweepy

# -- twitterBot Object
class TwitterBot:
    def __init__(self, consumerAPI: str, consumerSecret: str, token: str, secretToken: str):
        self.cAPI = consumerAPI
        self.cSecret = consumerSecret
        self.token = token
        self.sToken = secretToken
    def twitter(self):
        auth = tweepy.OAuthHandler(self.cAPI, self.cSecret)
        auth.set_access_token(self.token, self.sToken)
        tweepyAPI = tweepy.API(auth, wait_on_rate_limit=True, wait_on_rate_limit_notify=True)

        try:
            tweepyAPI.verify_credentials()
            print("> Authentication OK")
        except:
            print("> Error during Authentication")

        return tweepyAPI
    def tweetCheck(self, minutes, seconds, tm, ts):
        if (minutes == tm) and (seconds == ts):
            return True
        else:
            return False
    def tweet(self, twitter, price, image = False):
        message = f"The current price of XRP is {price} USD"
        try:
            if image is False:
                twitter.update_status(message)
            else:
                twitter.update_with_media(image, message)
        except:
            print('> error while tweeting')
