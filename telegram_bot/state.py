user_states = {}

DEFAULT_STATE = {
    ...
    # "content_message_id": None,  # сообщение с текстом
    # "control_message_id": None,  # сообщение с кнопками
    # "is_switching": False, # анти-дребезг
}


def get_user_state(chat_id):
    raise NotImplementedError(
        "Верните словарь состояния для chat_id, создав копию DEFAULT_STATE при первом обращении.\n"
        "Подумайте: как безопасно расширять DEFAULT_STATE без поломки старых инстансов?"
    )


def update_user_state(chat_id, **kwargs):
    pass


def clear_user_state(chat_id):
    pass
