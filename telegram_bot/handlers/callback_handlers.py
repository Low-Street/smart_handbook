from urllib.parse import quote
import requests
from telegram import InlineKeyboardMarkup, InlineKeyboardButton

from smart_handbook.api_clients.wikipedia_client import WikipediaClient
from telegram_bot.handlers.command_handlers import _cut
from telegram_bot.state import get_user_state, update_user_state

wikipedia_client = WikipediaClient()


async def handle_wiki_callback(update, context) -> None:
    pass
