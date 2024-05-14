import aiohttp

from config import USER_STATES
from utils.send_message import send_message
from keyboards import create_decision_keyboard


async def edit_post(session: aiohttp.ClientSession, user_id: int, message_id: int = 0, callback_data: str = None, message_text: str = None):
    if not message_id:
        if USER_STATES.get(user_id):
            USER_STATES.pop(user_id)
        return

    await send_message(session=session, chat_id=user_id, text=f'Enter the edited post text')
    USER_STATES[user_id] = 'AWAITING_EDITING'


async def edit_post_handler(session: aiohttp.ClientSession, chat_id: int, message_text: str = '', message_id: int = 0):
    if not message_id:
        if USER_STATES.get(chat_id):
            USER_STATES.pop(chat_id)
        return

    state = USER_STATES.get(chat_id)
    if state == 'AWAITING_EDITING':
        await send_message(session=session, chat_id=chat_id, text=message_text, reply_markup=await create_decision_keyboard())

    if USER_STATES.get(chat_id):
        USER_STATES.pop(chat_id)