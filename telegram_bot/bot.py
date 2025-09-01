import os
import logging
from pathlib import Path

from telegram.ext import Application, CommandHandler, CallbackQueryHandler, MessageHandler, filters
from telegram_bot.handlers.command_handlers import start_command, help_command, wiki_command, unknown_command
from telegram_bot.handlers.callback_handlers import handle_wiki_callback
from telegram import Update

# Настройка логирования
logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    level=logging.INFO
)
logger = logging.getLogger(__name__)


def main() -> None:
    """Запускает бота."""
    # Загрузка токена из переменной окружения
    pass


if __name__ == "__main__":
    # Убедитесь, что .env файл загружен, если используется python-dotenv
    try:
        from dotenv import load_dotenv

        ENV_PATH = Path(__file__).resolve().parents[1] / ".env"
        load_dotenv(ENV_PATH)
        logger.info(".env файл успешно загружен.")
    except ImportError:
        logger.warning("Модуль python-dotenv не найден. Переменные окружения должны быть установлены вручную.")

    main()
