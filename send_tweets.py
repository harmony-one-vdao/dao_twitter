from connection import *
from copy import deepcopy

from utils.tools import create_tweet_list, open_file


def post_to_twitter_facebook(send_data: dict, dry_run: bool = False) -> None:

    _tweets = create_tweet_list(send_data)

    for text in _tweets:
        media_path = send_data[text]
        if isinstance(media_path, list) and len(media_path) > 0:
            media_path = media_path.pop()
        log.info("-" * 80)
        log.info(
            f'attempting to post  ::  {text}  with {"No Media added" if not media_path else media_path}'
        )
        try:
            to_post = open_file(text)
            l = len(to_post)
            log.info(f"Tweet Length: {l}")
            if not dry_run:
                status = twitter_api.PostUpdate(to_post, media=media_path)
                log.info(f"Success!!\n\n{status.text}\n")
        except (FileNotFoundError, twitter.error.TwitterError) as e:
            log.error(f"ERROR  ::  {e}\n\n{to_post}\n")
        log.info(
            f"Sleeping for | {round(SLEEP / 60 / 60, 2)} Hours | {SLEEP // 60} Mins | {SLEEP} seconds |   "
        )
        sleep(SLEEP)


#### Uncomment to test single tweets..

# send_data = {

#    join(tweets_dir, "hip", "hip27.txt"): join(media_dir, "HIP", "HIP27.png"),
# #     join(tweets_dir, "election", "vdao1.txt"): None,
# }

# Run the Show..
while True:
    log.info("Starting New Tweet Cycle")
    data = deepcopy(send_data)
    post_to_twitter_facebook(data, dry_run=False)
    log.info("Ending Tweet Cycle.. Preparing new...")
