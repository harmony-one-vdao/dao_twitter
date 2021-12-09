from random import shuffle


def open_file(fn: str, remove_links: bool = False, reminder: bool = False) -> str:
    with open(fn, "r", encoding="utf8") as f:
        data = f.readlines()
        # print(data)
        if not remove_links:
            rtn = "".join(data)
        else:
            rtn = ""
            for x in data:
                if reminder:
                    if "Vote" in x.split():
                        x = "🚨 REMINDER: Validator DAO Vote 🚨\n"
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


def create_tweet_list(tweet_data: dict) -> list:
    _tweets = [x for x in tweet_data.keys()]
    done = []
    for x in _tweets:
        if isinstance(tweet_data[x], list) and x not in done:
            l = len(tweet_data[x])
            _tweets += [x for _ in range(1, l)]
            done.append(x)
    shuffle(_tweets)
    return _tweets


# l = open_file(r'C:\Users\John\Documents\GIT\Harmony\Validator Dao\dao_twitter\tweet_data\text\hip\hip12.txt', remove_links=True)
# print(l)
