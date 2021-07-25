from os.path import join
from time import sleep 

tweets_dir = join("tweet_data", "text")
media_dir = join("tweet_data", "media")


tweet_data = {
join(tweets_dir, 'HIP', 'hip8.txt'): join(media_dir, 'HIP', 'HIP8.png'),
join(tweets_dir, 'HIP', 'hip9.txt'): join(media_dir, 'HIP', 'HIP9.png'),
join(tweets_dir, 'HIP', 'hip10.txt'): join(media_dir, 'HIP', 'HIP10.png'),
join(tweets_dir, 'HIP', 'hip11.txt'): join(media_dir, 'HIP', 'HIP11.png'),
join(tweets_dir, 'HIP', 'hip12.txt'): join(media_dir, 'HIP', 'HIP12.png'),
join(tweets_dir, 'HIP', 'hip13.txt'): join(media_dir, 'HIP', 'HIP13.png'),
join(tweets_dir, 'HIP', 'hip14.txt'): join(media_dir, 'HIP', 'HIP14.png'),
join(tweets_dir, 'HIP', 'hip15.txt'): join(media_dir, 'HIP', 'HIP15.png'),
}

SLEEP = 24 / len(tweet_data.keys()) * 60
print(SLEEP)

# Generate
# for i in range(7, 16):
#     print(
#         "join(tweets_dir, 'HIP', 'hip{}.txt'): join(media_dir, 'HIP', 'HIP{}.png'),".format(
#             i, i
#         )
#     )
