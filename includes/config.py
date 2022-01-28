import sys
from os import environ
from os.path import join
from dotenv import load_dotenv, find_dotenv
import logging

file_handler = logging.FileHandler(filename=join("logs", "message.log"))
stdout_handler = logging.StreamHandler(sys.stdout)
handlers = [file_handler, stdout_handler]

logging.basicConfig(
    format="<%(filename)s> [%(levelname)s] - %(message)s",
    level=logging.INFO,
    handlers=handlers,
)

log = logging.getLogger()

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

# Telegram
api_id = environ["api_id"]
api_hash = environ["api_hash"]
