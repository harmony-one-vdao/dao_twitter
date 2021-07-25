from os.path import join
from time import sleep 

tweets_dir = join("tweet_data", "text")
media_dir = join("tweet_data", "media")


tweet_data = {
    # HIP Proposals
    join(tweets_dir, 'HIP', 'hip13.txt'): join(media_dir, 'hip', 'HIP13.png'),
join(tweets_dir, 'HIP', 'hip8.txt'): join(media_dir, 'hip', 'HIP8.png'),
join(tweets_dir, 'HIP', 'hip9.txt'): join(media_dir, 'hip', 'HIP9.png'),
join(tweets_dir, 'HIP', 'hip10.txt'): join(media_dir, 'hip', 'HIP10.png'),
join(tweets_dir, 'HIP', 'hip11.txt'): join(media_dir, 'hip', 'HIP11.png'),
join(tweets_dir, 'HIP', 'hip12.txt'): join(media_dir, 'hip', 'HIP12.png'),
join(tweets_dir, 'HIP', 'hip14.txt'): join(media_dir, 'hip', 'HIP14.png'),
join(tweets_dir, 'HIP', 'hip15.txt'): join(media_dir, 'hip', 'HIP15.png'),

# generic
join(tweets_dir, 'generic', 'dao_mission.txt'): join(media_dir, 'generic', 'Dao.png'),

# HIP Voting
}

SLEEP = 24 / len(tweet_data.keys()) * 60

# Generate
# for i in range(7, 16):
#     print(
#         "join(tweets_dir, 'HIP', 'hip{}.txt'): join(media_dir, 'hip', 'HIP{}.png'),".format(
#             i, i
#         )
#     )
