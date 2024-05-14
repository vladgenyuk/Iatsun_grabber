import asyncio
import aiohttp
from config import BOT_URL, USER_STATES, ADMIN_IDS
import handlers
from utils.grabber import read_channels
from utils.make_document import document_maker


async def get_updates(session, offset=None):
    url = BOT_URL + "/getUpdates"
    if offset:
        url += "?offset={}".format(offset)
    async with session.get(url) as resp:
        return await resp.json()


async def processor(session: aiohttp.ClientSession, update: dict):
    if update.get('callback_query'):
        chat_id: int = update.get('callback_query').get('from').get('id')
        callback_func_code = update.get('callback_query').get('data').split('-')[0]
        await callback_functions[callback_func_code](
            session=session,
            user_id=chat_id,
            callback_data=update.get('callback_query').get('data'),
            message_id=update.get('callback_query')['message']['message_id'],
            message_text=update.get('callback_query')['message']['text']
        )
        return
    elif update.get('message'):
        chat_id: int = update["message"]["chat"]["id"]
        if update.get('message').get('from') and update.get('message').get('from').get('first_name') == 'IATSUN':
            await handlers.grabber_handler(
                session=session,
                user_ids=ADMIN_IDS,
                message_text=update['message'].get('caption') or update['message'].get('text'),
                document=await document_maker(update=update)
            )
        elif update.get('message').get('text') and update.get('message').get('chat').get('id'):
            message: str = update["message"]["text"]
            if USER_STATES:
                await conversation_functions[USER_STATES.get(chat_id)](
                    session=session,
                    chat_id=chat_id,
                    message_text=message,
                    message_id=update['message']['message_id']
                )
                return
            if message.startswith('/'):
                if message in commands_functions.keys():
                    await commands_functions[message](
                        session=session,
                        chat_id=chat_id)
                    return

commands_functions = {
    '/start': handlers.start_handler,
    '/read_channels': handlers.read_channels_handler,
    '/overwrite': handlers.overwrite_pre_handler,
    '/read_groups': handlers.read_groups_handler,
}

callback_functions = {
    'delete': handlers.deletion_handler,
    'edit': handlers.edit_post,
    'publish': handlers.publish_handler
}

conversation_functions = {
    'AWAITING_OVERWRITE_PASSWORD': handlers.verify_overwrite_password,
    'AWAITING_FILE_TO_OVERWRITE': handlers.overwrite_file_handler,
    'AWAITING_EDITING': handlers.edit_post_handler
}


async def bot_loop():
    last_update_id = None
    async with aiohttp.ClientSession() as session:
        while True:
            updates = await get_updates(session, last_update_id)
            if 'result' in updates and len(updates['result']) > 0:
                for update in updates["result"]:
                    await processor(session=session, update=update)
                    last_update_id = update['update_id'] + 1


async def main():
    tasks = [bot_loop(), read_channels(search_term=None)]
    await asyncio.gather(*tasks)

if __name__ == '__main__':
    asyncio.run(main())
