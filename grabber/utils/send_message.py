import json
import aiohttp

from config import BOT_URL


async def send_message(session: aiohttp.ClientSession, chat_id, text, reply_markup: dict = None, document: dict = None):
    url = BOT_URL + f"/sendMessage"
    text = text if text else 'TEST'
    data = {
        'text': text,
        'chat_id': chat_id,
    }

    if reply_markup:
        data.update({'reply_markup': json.dumps(reply_markup)})

    if document:
        data.update({'media': document})

    async with session.post(url, data=data) as resp:
        pass
        # print(resp.status)