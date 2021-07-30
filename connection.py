from random import shuffle

import twitter
from includes.config import *
from includes.tweet_locations import *
from utils.tools import *

user = "1400948665859051520"  # DAO

api = twitter.Api(
    consumer_key=APIKey,
    consumer_secret=APISecretKey,
    access_token_key=AccessTokenKey,
    access_token_secret=AccessTokenSecret,
    tweet_mode="extended",
)


def get_statuses():
    statuses = api.GetUserTimeline(user)

    for s in statuses:
        print(s.full_text)
        print(s)
        print()

    return statuses


def post_tweets(dry_run=False):
    _tweets = [x for x in tweet_data.keys()]
    shuffle(_tweets)
    for text in _tweets:
        print(text)
        media_path = tweet_data[text]
        print("-" * 80)
        print(f"attempting to post  ::  {text}\n with {media_path}")
        try:
            to_post = open_file(text)
            l = len(to_post)
            print(l)
            if not dry_run:
                status = api.PostUpdate(to_post, media=media_path)
                print(f"Success!!\n\n{status.text}\n")
        except (FileNotFoundError, twitter.error.TwitterError) as e:
            print(f"ERRROR  ::  {e}\n\n{to_post}\n")
        print(f"sleeping for {SLEEP} seconds..")
        sleep(SLEEP)


# # get_statuses()
while True:
    post_tweets(dry_run=False)
