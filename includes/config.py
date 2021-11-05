from os import environ
from dotenv import load_dotenv

load_dotenv()

# Twitter
APIKey = environ["APIKey"]
APISecretKey = environ["APISecretKey"]
AccessTokenKey = environ["AccessTokenKey"]
AccessTokenSecret = environ["AccessTokenSecret"]

# Facebook
BearerToken = environ["BearerToken"]
BearerTokenDaoApp = environ["BearerTokenDaoApp"]
FB_ACCESS_TOKEN = environ["FB_ACCESS_TOKEN"]
PAGE_ID = r"265896568595660"
