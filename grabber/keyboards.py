async def create_decision_keyboard():
    kb = {
        "inline_keyboard": [
            [
                {
                    "text": f'✅ Опубликовать',
                    "callback_data": f"publish"
                },
                {
                    "text": f'   Редактировать',
                    "callback_data": f"edit"
                },
                {
                    "text": f'❌ Удалить',
                    "callback_data": f"delete"
                }
            ]
        ]
    }
    return kb