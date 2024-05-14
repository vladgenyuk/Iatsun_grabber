import aiohttp

from grabber.utils.send_message import send_message
from grabber.keyboards import create_decision_keyboard


async def decision_handler(session: aiohttp.ClientSession, chat_id: int):
    await send_message(session=session, chat_id=chat_id, text='Hello', reply_markup=await create_decision_keyboard())
