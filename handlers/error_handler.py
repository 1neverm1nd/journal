# handlers/error_handler.py

from telegram import Update
from telegram.ext import CallbackContext

async def handle_error(update: Update, context: CallbackContext):
    await context.bot.send_message(chat_id=update.effective_chat.id, text="Произошла ошибка. Попробуйте позже.")
