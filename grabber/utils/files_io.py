import json

from config import BASE_DIR


async def read_file(filename: str = f'{BASE_DIR}/channels.txt') -> str:
    with open(filename, 'r') as f:
        lines = []
        for l in f:
            lines.append(l)
    return ''.join(lines)


async def overwrite_file(filename: str = f'{BASE_DIR}/channels.txt', str_to_write: str = '@fordev'):
    with open(filename, 'w') as f:
        f.write(str_to_write)


async def overwrite_json(data: dict, filename: str = f'{BASE_DIR}/config.json'):
    with open(filename, 'w') as f:
        json.dump(data, f, indent=4)
