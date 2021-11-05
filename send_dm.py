from connection import *

hip = "hip14"

def get_message(hip: str) -> str:
    location = join(tweets_dir, "hip", f"{hip}.txt")
    message = open_file(location)
    return message
    

def get_users(hip:str) -> dict:    
    dm_list = join("tweet_data", "dm_list", f"{hip}.txt")
    users = open_file(dm_list).split('\n')
    print(users)
    return {x: twitter_api.GetUser(screen_name = x).id for x in users}
    


def send_direct_message(_id: int, msg: str) -> None:
    send_msg = twitter_api.PostDirectMessage(msg, _id, return_json=True)
    logging.info(f"Message Result:\n {send_msg}\n")


def run(hip: str) -> None:
    msg = get_message(hip)
    users = get_users(hip)
    for uname, id in users.items():
        logging.info(f'\tSending Message to:  [ {uname} ] with id [ {id} ] \n')
        send_direct_message(id, msg)

if __name__ == "__main__":
    # twitter_user = "MaffazO" 
    # id = twitter_api.GetUser(screen_name = twitter_user).id
    # msg = 'Vote Goddamit!!!'
    # send_direct_message(id, msg)

    run(hip)
