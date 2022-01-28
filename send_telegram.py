import asyncio
from telethon import TelegramClient, events
from connection import *
from utils.tools import get_blacklist, get_message, get_users

"""
If Telegram rate-limits the program will keep trying until all messages are exhausted.
Try playing with the delay if it is taking too long.. 
"""
hips = (
    # "hip0", # Test
    "hip25",
    "hip16",
    "vdao1",
)

_dir = "hip"

# Delay inbetween messages
DELAY = 0.2  # 5 per second


async def check_flood_and_sleep(e: str) -> None:
    if e.startswith("A wait of"):
        e = e.split()
        x = 0
        for x in e:
            try:
                s = int(x)
            except ValueError:
                pass
        log.info(
            f"Flooding the chat.  Sleeping for  {s // 60 // 60} Hours  |  {s // 60} Minutes  |  {s} Seconds.."
        )
        await asyncio.sleep(s)


async def main():
    client = TelegramClient(join("sessions", "vDao"), api_id, api_hash)
    await client.start()
    for hip in hips:
        sent = (
            []
        )  # keep track due to combining at_only and telegram lists (some users have the same username so we dont want to send 2 x)
        fails = ""
        msg = get_message(hip, _dir, **dict(reminder=True))
        users, dm_list = get_users(hip, "telegram_list", "\n")
        blacklist = get_blacklist()
        for user in users:
            if (
                user
                and user not in sent
                and user not in blacklist
                and "t.me" not in user.split("/")
            ):
                try:
                    await client.send_message(user, msg)
                    sent.append(user)
                except Exception as e:
                    e = str(e)
                    log.error(e)
                    fails += f"{user}\n"
                    log.error(f"Adding User {user}  to Fails list..")
                    await check_flood_and_sleep(e)
                await asyncio.sleep(DELAY)
        if fails:
            with open(dm_list, "w") as f:
                f.write(fails)


if __name__ == "__main__":
    try:
        asyncio.run(main())
    except RuntimeError as e:
        log.error(f"Loop Error.. Pleae fix at somepoint..")
