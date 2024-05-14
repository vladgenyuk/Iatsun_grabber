import aiohttp

from grabber.utils.send_message import send_message


async def start_handler(session: aiohttp.ClientSession, chat_id: int):
    await send_message(session=session, chat_id=chat_id, text='Hello')
