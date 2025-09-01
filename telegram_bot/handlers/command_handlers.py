import logging
from urllib.parse import quote

import requests
from telegram import InlineKeyboardMarkup, InlineKeyboardButton, Update
from telegram.ext import CallbackContext

from smart_handbook.api_clients.wikipedia_client import WikipediaClient
from telegram_bot.state import get_user_state, update_user_state, clear_user_state

logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    level=logging.INFO
)
logger = logging.getLogger(__name__)

wikipedia_client = WikipediaClient()
MAX_LEN = 3900  # немного с запасом до лимита ~4096


def _cut(t: str | None) -> str:
    pass


def _keyboard(state) -> InlineKeyboardMarkup:
    pass


def _get_chat_id(update):
    ec = getattr(update, "effective_chat", None)
    if ec and getattr(ec, "id", None) is not None:
        return ec.id
    msg = getattr(update, "message", None)
    if msg and getattr(msg, "chat", None) and getattr(msg.chat, "id", None) is not None:
        return msg.chat.id
    return None


async def start_command(update, context):
   pass


async def help_command(update, context):
    pass


async def wiki_command(update, context):
    pass


async def unknown_command(update, context) -> None:
    pass
