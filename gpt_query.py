# gpt_query.py

import sys
import time
from g4f.client import Client
from g4f.errors import RetryProviderError


def query_gpt(question):
    client = Client()

    while True:
        try:
            chat_completion = client.chat.completions.create(
                model="gpt-3.5-turbo",
                messages=[{"role": "user", "content": question}],
                stream=True
            )

            response = ''
            for completion in chat_completion:
                response += completion.choices[0].delta.content or ""

            # Проверяем, содержит ли ответ русские буквы
            if any('а' <= char.lower() <= 'я' for char in response):
                return response.strip()

        except RetryProviderError as e:
            print(f"Error occurred: {e}")
            print("Retrying with a different provider...")

        time.sleep(1)  # Добавьте задержку между попытками, чтобы избежать перегрузки провайдеров


def main():
    # Считываем вопрос из аргументов командной строки
    question = sys.argv[1] if len(sys.argv) > 1 else ""

    answer = query_gpt(question)

    # Выводим ответ на стандартный вывод для передачи его в C#
    print(answer)


if __name__ == "__main__":
    main()
