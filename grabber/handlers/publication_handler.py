import aiohttp

from grabber.utils.delete_message import delete_message
from grabber.utils.publish_post import validate_and_publish_post


async def publish_handler(session: aiohttp.ClientSession, message_id: int, user_id: int, message_text: str, callback_data: str = None):
    await validate_and_publish_post(session=session, message_text=message_text)
    await delete_message(session=session, message_id=message_id, user_id=user_id)
