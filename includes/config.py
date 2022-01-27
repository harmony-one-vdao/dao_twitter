from os import environ
from os.path import join
from dotenv import load_dotenv, find_dotenv
import logging

logging.basicConfig(format="[%(levelname)s] - %(message)s", level=logging.INFO)


d = load_dotenv(find_dotenv())
print(f"Env file Found?  ::  {d}")

num_days_cycle = 3

tweets_dir = join("send_data", "text")
media_dir = join("send_data", "media")

# Twitter
APIKey = environ["APIKey"]
APISecretKey = environ["APISecretKey"]
AccessTokenKey = environ["AccessTokenKey"]
AccessTokenSecret = environ["AccessTokenSecret"]

# # Facebook
# BearerToken = environ["BearerToken"]
# BearerTokenDaoApp = environ["BearerTokenDaoApp"]
# FB_ACCESS_TOKEN = environ["FB_ACCESS_TOKEN"]
# PAGE_ID = r"265896568595660"

# Email
EMAIL_SMTP = environ["EMAIL_SMTP"]
EMAIL_FROM = environ["EMAIL_FROM"]
EMAIL_PASS = environ["EMAIL_PASS"]
