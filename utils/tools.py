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


# l = open_file(r'C:\Users\John\Documents\GIT\Harmony\Validator Dao\dao_twitter\tweet_data\text\hip\hip12.txt', remove_links=True)
# print(l)
