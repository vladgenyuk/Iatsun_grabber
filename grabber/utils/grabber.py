import asyncio

from telethon import TelegramClient
from telethon.tl.types import InputDocument, InputPhoto

from utils.files_io import read_file, overwrite_json
from config import API_ID, API_HASH, DELAY_GRABBER, LIMIT, LAST_IDS, ADMIN_IDS, BOT_USERNAME


async def read_channels(search_term: str | None, limit: int = LIMIT):
    channels_to_read = (await read_file()).split()
    while True:
        async with TelegramClient('session_name', API_ID, API_HASH) as client:
            await asyncio.sleep(DELAY_GRABBER)

            for channel in channels_to_read:
                channel = await client.get_entity(channel)

                posts = client.iter_messages(
                    entity=channel,
                    limit=limit,
                    search=search_term,
                    min_id=LAST_IDS.get(f'@{channel.username}', 1),
                )

                post = None

                async for post in posts:
                    post = post.to_dict()
                    if not post.get('message'):
                        continue

                    if post.get('media') and (post.get('media').get('photo') or post.get('media').get('document')):
                        if post.get('media').get('document'):
                            doc = InputDocument(post['media']['document']['id'],
                                                post['media']['document']['access_hash'],
                                                post['media']['document']['file_reference'])
                            await client.send_file(BOT_USERNAME, doc, caption=post.get('message'))

                        elif post.get('media').get('photo'):
                            photo = InputPhoto(post['media']['photo']['id'],
                                               post['media']['photo']['access_hash'],
                                               post['media']['photo']['file_reference'])
                            await client.send_file(BOT_USERNAME, photo, caption=post.get('message'))
                        else:
                            await client.send_message(BOT_USERNAME, post.get('message'))

                    else:
                        await client.send_message(BOT_USERNAME, post.get('message'))

                if post:
                    data = dict()
                    LAST_IDS[f'@{channel.username}'] = post.get('id')
                    data['last_ids'] = LAST_IDS
                    data['admin_ids'] = ADMIN_IDS
                    await overwrite_json(data)

