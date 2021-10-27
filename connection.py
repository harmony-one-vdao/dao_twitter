from random import shuffle

import twitter
from includes.tweet_locations import *
from includes.config import *
from utils.tools import *

# from post_facebook import *


import logging

twitter_user = "1400948665859051520"  # DAO

twitter_api = twitter.Api(
    consumer_key=APIKey,
    consumer_secret=APISecretKey, 
    access_token_key=AccessTokenKey,
    access_token_secret=AccessTokenSecret,
    tweet_mode="extended",
)


def get_statuses():
    statuses = twitter_api.GetUserTimeline(twitter_user)

    for s in statuses:
        logging.info(s.full_text)
        logging.info(s)
        logging.info()

    return statuses


def post_to_twitter_facebook(dry_run=False):
    _tweets = [x for x in tweet_data.keys()]
    shuffle(_tweets)
    for text in _tweets:
        media_path = tweet_data[text]
        logging.info("-" * 80)
        logging.info(
            f'attempting to post  ::  {text}  with {"No Media added" if not media_path else media_path}'
        )
        try:
            to_post = open_file(text)
            l = len(to_post)
            logging.info(f"Tweet Length: {l}")
            if not dry_run:
                status = twitter_api.PostUpdate(to_post, media=media_path)
                logging.info(f"Success!!\n\n{status.text}\n")
        except (FileNotFoundError, twitter.error.TwitterError) as e:
            logging.error(f"ERROR  ::  {e}\n\n{to_post}\n")
        logging.info(f"sleeping for {SLEEP} seconds..")
        sleep(SLEEP)


# # get_statuses()
while True:
    logging.info("Starting New Tweet Cycle")
    post_to_twitter_facebook(dry_run=False)
    logging.info("Ending Tweet Cycle.. Preparing new...")
