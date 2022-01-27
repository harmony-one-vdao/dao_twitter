import asyncio
from telethon import TelegramClient, events

# These example values won't work. You must get your own api_id and
# api_hash from https://my.telegram.org, under API Development.
api_id = 13320405
api_hash = "6f2be7d76fe2af0a988cdab33e35386e"


async def main():
    # The first parameter is the .session file name (absolute paths allowed)
    async with TelegramClient("vDAO", api_id, api_hash).start() as client:
        await client.send_message("MaffazOne", "Hello, myself!")


asyncio.run(main())
