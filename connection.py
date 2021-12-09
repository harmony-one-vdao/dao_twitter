import twitter
from includes.tweet_locations import *
from includes.config import *

twitter_api = twitter.Api(
    consumer_key=APIKey,
    consumer_secret=APISecretKey,
    access_token_key=AccessTokenKey,
    access_token_secret=AccessTokenSecret,
    tweet_mode="extended",
)
