import aiohttp

from grabber.utils.send_message import send_message
from grabber.utils.files_io import read_file


async def read_channels_handler(session: aiohttp.ClientSession, chat_id: int):
    channels = await read_file()
    await send_message(session=session, chat_id=chat_id, text=f'It is your channels:\n{channels}')