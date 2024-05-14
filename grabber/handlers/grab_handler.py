import aiohttp

from utils.send_message import send_message
from utils.send_media_group import send_media_group
from utils.send_photo import send_photo
from utils.send_video import send_video

from keyboards import create_decision_keyboard


async def grabber_handler(session: aiohttp.ClientSession, message_text: str, user_ids: list[int], document: list[dict] | dict = None):
    for user_id in user_ids:
        if document:
            if isinstance(document, list):
                if document[0].get('type') == 'photo' or document[0].get('type') == 'video':
                    await send_media_group(session=session, chat_id=user_id, media=document, reply_markup=await create_decision_keyboard())

            elif document.get('type') == 'video':
                await send_video(session=session, text=document.get('caption'), chat_id=user_id, reply_markup=await create_decision_keyboard())

            elif document.get('type') == 'photo':
                await send_photo(session=session, text=document.get('caption'), chat_id=user_id, reply_markup=await create_decision_keyboard())

        else:
            await send_message(session=session, text=message_text, chat_id=user_id, reply_markup=await create_decision_keyboard())
