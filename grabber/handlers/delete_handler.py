import aiohttp

from grabber.utils.delete_message import delete_message


async def deletion_handler(session: aiohttp.ClientSession, message_id: int, user_id: int, callback_data: str = None, message_text: str = None):
    await delete_message(session=session, message_id=message_id, user_id=user_id)
