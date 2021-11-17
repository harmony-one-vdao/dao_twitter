from connection import *

hips = ("hip14", "hip15")

# Delay inbetween tweets
DELAY = 1
# Big sleep if Twitter gives a Spam error.
TAKE_A_BREAK = 1200

def get_message(hip: str) -> str:
    location = join(tweets_dir, "hip", f"{hip}.txt")
    message = open_file(location, remove_links=True)
    logging.info(message)
    return message


def get_users(hip: str) -> dict:
    dm_list = join("tweet_data", "dm_list", f"{hip}.txt")
    users = open_file(dm_list).split("\n")
    rtn = {}
    for x in users:
        if x:
            x = x.split('@')[-1]
            try:
                rtn.update({x: twitter_api.GetUser(screen_name=x).id})
            except twitter.error.TwitterError as e:
                logging.error(f"Problem with User [ {x} ]\n{e}")
                rtn.update({x:0})
    return rtn


def send_direct_message(_id: int, msg: str) -> None:
    try:
        msg = twitter_api.PostDirectMessage(msg, _id, return_json=True)
        return msg
    except twitter.error.TwitterError as e:
        return {"errors": e}


def run(hip: str) -> None:
    msg = get_message(hip)
    users = get_users(hip)

    retry = []
    cannot_msg = []
    not_followed_by = []
    user_not_found = []

    for uname, id in users.items():
        if id == 0:  # User not found.
            user_not_found.append(uname)
            continue

        logging.info(f"\tSending Message to:  [ {uname} ] with id [ {id} ] \n")
        result = send_direct_message(id, msg)

        if not result.get("errors"):
            logging.info(f"Message Result:  {result}\n")

        elif result.get("errors"):
            logging.error(f"Message ERROR:   {result}\n")

            if (
                result["errors"][0]["code"] == 226
            ):  # This request looks like it might be automated.
                retry.append(uname)
                sleep(
                    TAKE_A_BREAK
                )  # take a break from automation if twitter does not like it..

            elif (
                result["errors"][0]["code"] == 349
            ):  # You cannot send messages to this user.
                cannot_msg.append(uname)

            elif (
                result["errors"][0]["code"] == 326
            ):  # You are sending a Direct Message to users that do not follow you.'
                not_followed_by.append(uname)
            else:
                logging.error(f"Dunno what happened, adding to failures..\n{result}\n")
                retry.append(uname)

        sleep(DELAY)  # arbitrary time to pause between messages

    save_error_or_failed_dms('', hip, retry)
    save_error_or_failed_dms(hip, "cannot_msg", cannot_msg)
    save_error_or_failed_dms(hip, "user_not_found", user_not_found)
    save_error_or_failed_dms(hip, "notFollowed_by", not_followed_by)


def save_error_or_failed_dms(hip: str, _type: str, data: list) -> None:
    sep = '-'
    if not hip:
        sep = ''
    dm_list = join("tweet_data", "dm_list", f"{hip}{sep}{_type}.txt")
    with open(dm_list, "w") as f:
        for x in data:
            f.write(f"@{x}\n")


if __name__ == "__main__":
    for hip in hips:
        run(hip)
