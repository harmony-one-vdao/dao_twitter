from connection import *
from copy import deepcopy

from utils.tools import create_tweet_list, open_file


def post_to_twitter_facebook(tweet_data: dict, dry_run: bool = False) -> None:

    _tweets = create_tweet_list(tweet_data)

    for text in _tweets:
        media_path = tweet_data[text]
        if isinstance(media_path, list) and len(media_path) > 0:
            media_path = media_path.pop()
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
        logging.info(
            f"Sleeping for | {round(SLEEP / 60 / 60, 2)} Hours | {SLEEP // 60} Mins | {SLEEP} seconds |   "
        )
        sleep(SLEEP)


while True:
    logging.info("Starting New Tweet Cycle")
    data = deepcopy(tweet_data)
    post_to_twitter_facebook(data, dry_run=False)
    logging.info("Ending Tweet Cycle.. Preparing new...")
