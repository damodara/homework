import json
from typing import List

import src.external_api as external_api


def load_transactions(file_path: str) -> List[dict]:
    """
    Загружает данные о финансовых транзакциях из указанного JSON-файла.
    Возвращает список словарей с данными транзакций.
    Если файл отсутствует, пуст или содержит неверные данные,
    возвращается пустой список.

    :param file_path: Путь до JSON-файла
    :return: Список словарей с данными транзакций
    """
    try:
        with open(file_path, encoding="utf-8") as file:
            data = json.load(file)

        # Проверяем, что файл содержит именно список объектов
        if isinstance(data, list):
            return data
        else:
            return []
    except FileNotFoundError:
        # Файл не найден
        return []
    except json.JSONDecodeError:
        # Ошибка в структуре JSON
        return []
    # except Exception as e:
    #     # Любые другие непредвиденные исключения
    #     print(f"Произошла ошибка: {e}")
    #     return []


def process_transaction(transaction: dict) -> float:
    """
    Обрабатывает транзакцию, конвертируя сумму в рубли, если валюта не равна RUB.
    :param transaction: Словарь с информацией о транзакции
    :return: Сумма транзакции в рублях
    """
    amount = transaction["operationAmount"]["amount"]
    currency = transaction["operationAmount"]["currency"]["code"].upper()

    if currency == "RUB":
        return float(amount)
    else:
        return float(external_api.convert_currency(amount, currency))
