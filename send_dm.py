from random import shuffle

import twitter
from includes.tweet_locations import *
from includes.config import *
from utils.tools import *

# from post_facebook import *

import logging

twitter_user = "MaffazO" 

twitter_api = twitter.Api(
    consumer_key=APIKey,
    consumer_secret=APISecretKey, 
    access_token_key=AccessTokenKey,
    access_token_secret=AccessTokenSecret,
    tweet_mode="extended",
)

id = twitter_api.GetUser(screen_name = twitter_user).id
msg = 'Vote Goddamit!!!'


def get_statuses(id):
    statuses = twitter_api.GetUserTimeline(id)

    for s in statuses:
        logging.info(s.full_text)
        logging.info(s)

    return statuses

def send_direct_message(_id, msg):
    send_msg = twitter_api.PostDirectMessage(msg, _id, return_json=True)
    logging.info(send_msg)

send_direct_message(id, msg)