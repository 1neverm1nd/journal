
from telegram import Update
from telegram.ext import Application, MessageHandler, CommandHandler, filters
from bot_config import TELEGRAM_TOKEN
from handlers.message_handler import handle_message
from handlers.error_handler import handle_error

def main():
    # Создаем приложение бота
    application = Application.builder().token(TELEGRAM_TOKEN).build()

    # Добавляем обработчик для сообщений
    application.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, handle_message))

    # Добавляем обработчик ошибок
    application.add_error_handler(handle_error)

    # Запускаем бота
    application.run_polling()
    print("Bot is running...")

if __name__ == "__main__":
    main()
