from random import shuffle
from includes.config import *


def open_file(fn: str, remove_links: bool = False, reminder: bool = False) -> str:
    with open(fn, "r", encoding="utf8") as f:
        data = f.readlines()
        # print(data)
        if not remove_links and not reminder:
            rtn = "".join(data)
        else:
            rtn = ""
            for x in data:
                if reminder:
                    if "Vote" in x.split():
                        x = "🚨 REMINDER: Validator DAO Vote 🚨\n"
                if remove_links:
                    if x.startswith(("✍️", "Talk", "🗳️")):
                        break
                else:
                    rtn += x
        return rtn


def calc_extra_images(d: dict) -> int:
    extra = 0
    for v in d.values():
        if isinstance(v, list):
            extra += len(v) - 1
    return extra


def create_tweet_list(send_data: dict) -> list:
    _tweets = [x for x in send_data.keys()]
    done = []
    for x in _tweets:
        if isinstance(send_data[x], list) and x not in done:
            l = len(send_data[x])
            _tweets += [x for _ in range(1, l)]
            done.append(x)
    shuffle(_tweets)
    return _tweets


def get_message(hip: str, _dir: str, **kw) -> str:
    location = join(tweets_dir, _dir, f"{hip}.txt")
    message = open_file(location, **kw)
    logging.info(message)
    return message


# l = open_file(r'C:\Users\John\Documents\GIT\Harmony\Validator Dao\dao_twitter\send_data\text\hip\hip12.txt', remove_links=True)
# print(l)
