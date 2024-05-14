import json
import aiohttp
from config import BOT_URL


async def send_media_group(session: aiohttp.ClientSession, chat_id: int, media: list[dict], reply_markup: dict = None):
    url = f"{BOT_URL}/sendMediaGroup"

    data = {
        "chat_id": chat_id,
        'media': media
    }

    if reply_markup:
        data.update({'reply_markup': json.dumps(reply_markup)})

    async with session.post(url, json=data) as resp:
        pass
        # print(resp.status)
