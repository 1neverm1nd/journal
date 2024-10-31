# services/ai_service.py

import openai
from bot_config import OPENAI_API_KEY, OPENAI_SETTINGS

openai.api_key = OPENAI_API_KEY

def generate_journal_sections(topic):
    # Формируем запрос для генерации текста
    messages = [
        {"role": "system", "content": "You are a helpful assistant for generating scientific articles."},
        {"role": "user", "content": (
            f"Создай научную статью на тему '{topic}' с разделами:\n\n"
            "1. Название\n"
            "2. Аннотация\n"
            "3. Ключевые слова\n"
            "4. Введение\n"
            "5. Методы\n"
            "6. Результаты\n"
            "7. Обсуждение\n"
            "8. Заключение\n"
            "9. Список литературы"
        )}
    ]

    try:
        response = openai.ChatCompletion.create(
            model=OPENAI_SETTINGS["model"],
            messages=messages,
            max_tokens=OPENAI_SETTINGS["max_tokens"],
            temperature=OPENAI_SETTINGS["temperature"]
        )
        journal_text = response.choices[0].message['content'].strip()
        return journal_text
    except Exception as e:
        print(f"Ошибка при генерации текста: {e}")
        return "Ошибка при генерации статьи. Попробуйте позже."
