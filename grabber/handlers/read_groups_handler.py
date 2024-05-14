import aiohttp

from grabber.utils.grabber import read_channels


async def read_groups_handler(session: aiohttp.ClientSession, message_id: int, user_id: int, callback_data: str = None):
    await read_channels(search_term=None)
