import twitter
from includes.config import *
from includes.tweet_locations import *
from utils.tools import *

user = "1400948665859051520" # DAO

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
    for to_post, media_path in tweet_data.items():
        print('-'*80)
        try:
            to_post = open_file(to_post)
            l = len(to_post)
            print(l)
            if not dry_run:
                status = api.PostUpdate(to_post, media=media_path)
                print(f'Success!!\n\n{status.text}\n')
        except (FileNotFoundError, twitter.error.TwitterError) as e:
            print(f'ERRROR  ::  {e}\n\n{to_post}\n')
        print(f'sleeping for {SLEEP} seconds..')
        sleep(SLEEP)


# # get_statuses()
while True:
    post_tweets(dry_run=False)
