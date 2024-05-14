async def document_maker(update: dict) -> dict | list:

    if update.get('message').get('video'):
        videos = []
        if isinstance(update.get('message').get('video'), dict):
            return [{'type': 'video', 'media': update.get('message').get('video').get('file_id'), 'caption': update.get('message').get('caption')}]

        for c, i in enumerate(update.get('message').get('video')):
            if c == 0:
                videos.append({'type': 'video', 'media': i.get('file_id'), 'caption': update.get('message').get('caption')})
            else:
                videos.append({'type': 'video', 'media': i.get('file_id'), 'caption': ''})

        return videos

    if update.get('message').get('photo'):
        photos = []
        if isinstance(update.get('message').get('photo'), dict):
            return [{'type': 'photo', 'media': update.get('message').get('photo').get('file_id'), 'caption': update.get('message').get('caption')}]

        for c, i in enumerate(update.get('message').get('photo')):
            if c == 0:
                photos.append(
                    {'type': 'photo', 'media': i.get('file_id'), 'caption': update.get('message').get('caption')})
            else:
                photos.append({'type': 'photo', 'media': i.get('file_id'), 'caption': ''})
        return photos
