import aiohttp
import json

from grabber.config import BOT_URL


async def update_message_text(session: aiohttp.ClientSession, chat_id: int, message_id: int, text: str, reply_markup: dict = None, web_page_preview: dict = None):
    url = f"{BOT_URL}/editMessageText"

    params = {
        'chat_id': chat_id,
        'message_id': message_id,
        'text': text,
    }

    if reply_markup is not None:
        params.update({'reply_markup': json.dumps(reply_markup)})

    if web_page_preview is not None:
        params.update({'web_page_preview': json.dumps(web_page_preview)})

    async with session.post(url, params=params) as resp:
        pass