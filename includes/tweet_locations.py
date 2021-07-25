from os.path import join
from time import sleep 

tweets_dir = join("tweet_data", "text")
media_dir = join("tweet_data", "media")


tweet_data = {
    # HIP Proposals
    join(tweets_dir, 'hip' 'hip13.txt'): join(media_dir, 'HIP', 'HIP13.png'),
join(tweets_dir, 'hip' 'hip8.txt'): join(media_dir, 'HIP', 'HIP8.png'),
join(tweets_dir, 'hip' 'hip9.txt'): join(media_dir, 'HIP', 'HIP9.png'),
join(tweets_dir, 'hip' 'hip10.txt'): join(media_dir, 'HIP', 'HIP10.png'),
join(tweets_dir, 'hip' 'hip11.txt'): join(media_dir, 'HIP', 'HIP11.png'),
join(tweets_dir, 'hip' 'hip12.txt'): join(media_dir, 'HIP', 'HIP12.png'),
join(tweets_dir, 'hip' 'hip14.txt'): join(media_dir, 'HIP', 'HIP14.png'),
join(tweets_dir, 'hip' 'hip15.txt'): join(media_dir, 'HIP', 'HIP15.png'),

# generic
join(tweets_dir, 'generic', 'dao_mission.txt'): join(media_dir, 'generic', 'Dao.png'),

# HIP Voting
}

SLEEP = 24 / len(tweet_data.keys()) * 60

# Generate
# for i in range(7, 16):
#     print(
#         "join(tweets_dir, 'hip' 'hip{}.txt'): join(media_dir, 'HIP', 'HIP{}.png'),".format(
#             i, i
#         )
#     )
