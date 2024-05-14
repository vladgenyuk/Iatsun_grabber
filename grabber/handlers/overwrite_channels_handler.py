import aiohttp

from grabber.config import USER_STATES, BOT_OVERWRITE_PASSWORD
from grabber.utils.send_message import send_message
from grabber.utils.files_io import read_file, overwrite_file


async def overwrite_pre_handler(session: aiohttp.ClientSession, chat_id: int, **kwargs):
    await send_message(session=session, chat_id=chat_id, text=f'Enter password to overwrite file with channels')
    USER_STATES[chat_id] = 'AWAITING_OVERWRITE_PASSWORD'


async def verify_overwrite_password(session: aiohttp.ClientSession, chat_id: int, message_text: str, message_id: int = 0):
    state = USER_STATES.get(chat_id)

    if state == 'AWAITING_OVERWRITE_PASSWORD':
        if message_text == BOT_OVERWRITE_PASSWORD:
            await send_message(session=session, chat_id=chat_id, text=f'Password is correct, now write your channels line by line, it is tour file:')
            await send_message(session=session, chat_id=chat_id, text=await read_file())
            USER_STATES[chat_id] = 'AWAITING_FILE_TO_OVERWRITE'
        else:
            await send_message(session=session, chat_id=chat_id, text=f'Password is incorrect')

            if USER_STATES.get(chat_id):
                USER_STATES.pop(chat_id)


async def overwrite_file_handler(session: aiohttp.ClientSession, chat_id: int, message_text: str = '@fordev', message_id: int = 0):
    state = USER_STATES.get(chat_id)

    if state == 'AWAITING_FILE_TO_OVERWRITE':
        await overwrite_file(str_to_write=message_text)
        await send_message(session=session, chat_id=chat_id, text='channels.txt file has been overwritten')

    if USER_STATES.get(chat_id):
        USER_STATES.pop(chat_id)
