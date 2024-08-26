# Импорт необходимых модулей
from gemini import Gemini

# Пример 1: Инициализация клиента с автоматическим сбором куки
client = Gemini(auto_cookies=True)

# Установка языка ответа Gemini на русский
import os
os.environ["GEMINI_LANGUAGE"] = "RU"  # Установка языка ответа на русский
os.environ["GEMINI_ULTRA"] = "1"      # Включение расширенного режима Gemini (опционально)

# Пример 2: Отправка текстового промпта и получение ответа
response = client.generate_content("Привет, Gemini. Какая погода в Москве сегодня?")
print(response.payload)

# Пример 3: Инициализация клиента с куками из файла (если требуется)
cookies = {
    "__Secure-1PSIDCC": "value",
    "__Secure-1PSID": "value",
    "__Secure-1PSIDTS": "value",
    "NID": "value",
}

client = Gemini(cookies=cookies)

# Генерация контента с новым клиентом
response = client.generate_content("Расскажи мне о больших языковых моделях.")
print(response.payload)

# Пример 4: Отправка запроса и получение текста ответа и статус-кода
response_text, response_status = client.send_request("Привет, Gemini. Расскажи мне о больших языковых моделях.")
print(response_text)
print(response_status)

# Пример 5: Генерация текста и вывод результата
prompt = "Привет, Gemini. Расскажи мне о больших языковых моделях."
response = client.generate_content(prompt)
print(response.text)

# Пример 6: Использование сервисов Google для генерации контента
response = client.generate_content("@YouTube Найди видео, связанные с Google Gemini")
print(response.response_dict)

# Пример 7: Указание идентификатора кандидата ответа (RCID) и генерация нового контента
response1 = client.generate_content("Расскажи мне об истории России.")
client.rcid = "rc_xxxx"  # Установите RCID из предыдущего ответа
response2 = client.generate_content("Сколько времени займет поездка от Москвы до Санкт-Петербурга?")
print(response2.payload)

# Пример 8: Изменение выбранного ответа с 0 на n
from gemini import GeminiModelOutput

GeminiModelOutput.chosen = 1  # Выберите первый ответ
response_choice_1 = client.generate_content("Расскажи мне об истории России.")
print(response_choice_1.payload)

# Пример 9: Генерация пользовательского контента с использованием пользовательского парсера
response_text, response_status = client.send_request("Расскажи мне об истории России.")
response = client.generate_custom_content("Расскажи мне об истории России.", *custom_parser)
print(response.payload)

# Пример 10: Использование вращающихся прокси для избежания блокировок запросов
proxy_url = "http://xxxxx:@smartproxy.crawlbase.com:8012"
proxies = {"http": proxy_url, "https": proxy_url}

client = Gemini(cookies=cookies, proxies=proxies, timeout=30, verify=False)
client.session.header["crawlbaseAPI-Parameters"] = "country=RU"
response = client.generate_content("Привет, Gemini. Покажи красивое фото природы России.")
print(response.payload)
