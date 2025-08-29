import os

import requests
from dotenv import load_dotenv

load_dotenv()
API_TOKEN = os.getenv("API_KEY")
HEADERS = {"apikey": API_TOKEN}


def convert_currency(amount: float, from_currency: str, to_currency: str = "RUB") -> float:
    """
    Конвертирует указанную сумму из одной валюты в другую используя внешний API. Возвращает результат в указанной валюте.
    :param amount: Сумма для конвертации
    :param from_currency: Валюта исходной суммы (USD/EUR и др.)
    :param to_currency: Валюта результата (по умолчанию RUB)
    :return: Результат конвертации
    """
    BASE_URL = (
        f"https://api.apilayer.com/exchangerates_data/convert?to={to_currency}&from={from_currency}&amount={amount}"
    )
    response = requests.get(BASE_URL, headers=HEADERS)
    response.raise_for_status()
    data = response.json()
    return float(data["result"])
