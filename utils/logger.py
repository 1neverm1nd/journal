
import logging

logging.basicConfig(
    filename='bot.log',
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s'
)

def log_message(chat_id, message):
    logging.info(f"Сообщение от {chat_id}: {message}")
