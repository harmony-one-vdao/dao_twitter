from os.path import join
from time import sleep

tweets_dir = join("tweet_data", "text")
media_dir = join("tweet_data", "media")


tweet_data = {
    # HIP Proposals
    join(tweets_dir, "hip", "hip13.txt"): join(media_dir, "HIP", "HIP13.png"),
    join(tweets_dir, "hip", "hip9.txt"): join(media_dir, "HIP", "HIP9.png"),
    join(tweets_dir, "hip", "hip10.txt"): join(media_dir, "HIP", "HIP10.png"),
    join(tweets_dir, "hip", "hip11.txt"): join(media_dir, "HIP", "HIP11.png"),
    join(tweets_dir, "hip", "hip12.txt"): join(media_dir, "HIP", "HIP12.png"),
    join(tweets_dir, "hip", "hip14.txt"): join(media_dir, "HIP", "HIP14.png"),
    join(tweets_dir, "hip", "hip15.txt"): join(media_dir, "HIP", "HIP15.png"),
    join(tweets_dir, "hip", "hip16.txt"): join(media_dir, "HIP", "HIP16.png"),
    # generic
    join(tweets_dir, "generic", "dao_mission.txt"): join(
        media_dir, "generic", "Dao.png"
    ),
    join(tweets_dir, "generic", "agenda.txt"): join(media_dir, "generic", "Dao.png"),
    join(tweets_dir, "generic", "goals.txt"): join(media_dir, "generic", "Dao.png"),
    join(tweets_dir, "generic", "become_validator.txt"): join(
        media_dir, "generic", "new_validators.jpg"
    ),
    # medium articles
    join(tweets_dir, "medium_articles", "volumes_expand.txt"): None,
    join(tweets_dir, "medium_articles", "what_is_vdao.txt"): None,
    join(tweets_dir, "medium_articles", "updating_node.txt"): None,
    # HIP Voting links
}

num_tweets = len(tweet_data.keys())
num_days_cycle = 2.5
hours_between_tweets = (num_days_cycle * 24) / num_tweets
seconds_between_tweet = hours_between_tweets * 60


SLEEP = round(seconds_between_tweet)

p = {
    "num_days_cycle": num_days_cycle,
    "hours_between_tweets": hours_between_tweets,
    "num_tweets": num_tweets,
    "seconds_between_tweet": seconds_between_tweet,
    "SLEEP (secs)": SLEEP,
}


for k, v in p.items():
    # print(f"{k}  ::  {v}")
    print(f"{' '.join(k.split('_')).title():<50}  ::   {v:<30}")


# Generate
# for i in range(7, 16):
#     print(
#         "join(tweets_dir, 'hip', 'hip{}.txt'): join(media_dir, 'HIP', 'HIP{}.png'),".format(
#             i, i
#         )
#     )
