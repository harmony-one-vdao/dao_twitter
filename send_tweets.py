from connection import *


def post_to_twitter_facebook(dry_run: bool = False) -> None:
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


while True:
    logging.info("Starting New Tweet Cycle")
    post_to_twitter_facebook(dry_run=False)
    logging.info("Ending Tweet Cycle.. Preparing new...")
