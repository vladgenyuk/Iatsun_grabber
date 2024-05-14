import aiohttp

from grabber.config import BOT_URL


async def delete_message(session: aiohttp.ClientSession, user_id: int, message_id: int):
    url = BOT_URL + "/deleteMessage"

    params = {
        'chat_id': user_id,
        'message_id': message_id
    }

    async with session.post(url, params=params) as resp:
        pass