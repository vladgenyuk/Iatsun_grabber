import aiohttp
import json

from grabber.config import CHANNEL_ID, BOT_TOKEN


async def validate_and_publish_post(session: aiohttp.ClientSession, message_text: str = '', reply_markup: dict = None):
    url = f'https://api.telegram.org/bot{BOT_TOKEN}/sendMessage'

    if not message_text:
        return

    data = {
        'text': message_text,
        'chat_id': CHANNEL_ID
    }

    if reply_markup is not None:
        data.update({'reply_markup': json.dumps(reply_markup)})

    async with session.post(url, data=data) as resp:
        pass
        # print(await resp.json())
