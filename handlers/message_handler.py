# handlers/message_handler.py

from telegram import Update
from telegram.ext import CallbackContext
from utils.logger import log_message
from services.ai_service import generate_journal_sections

async def handle_message(update: Update, context: CallbackContext):
    user_message = update.message.text
    chat_id = update.effective_chat.id

    # Логируем сообщение
    log_message(chat_id, user_message)

    # Генерируем текст статьи
    response = f"Вы ввели тему: '{user_message}'. Генерация статьи началась..."
    await context.bot.send_message(chat_id=chat_id, text=response)

    # Генерация статьи и отправка результата
    journal_text = generate_journal_sections(user_message)
    await context.bot.send_message(chat_id=chat_id, text=journal_text)
