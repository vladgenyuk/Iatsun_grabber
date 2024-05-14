import json
import aiohttp

from grabber.config import BOT_URL


async def send_video(session: aiohttp.ClientSession, chat_id, text, reply_markup: dict = None, document: str = None):
    url = BOT_URL + f"/sendVideo"

    data = {
        'caption': text,
        'chat_id': chat_id,
        'video': document
    }

    if reply_markup:
        data.update({'reply_markup': json.dumps(reply_markup)})

    async with session.post(url, json=data) as resp:
        pass
        # print(resp.status)
