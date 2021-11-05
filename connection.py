from random import shuffle

import twitter
from includes.tweet_locations import *
from includes.config import *
from utils.tools import *

# from post_facebook import *

import logging

twitter_api = twitter.Api(
    consumer_key=APIKey,
    consumer_secret=APISecretKey,
    access_token_key=AccessTokenKey,
    access_token_secret=AccessTokenSecret,
    tweet_mode="extended",
)
