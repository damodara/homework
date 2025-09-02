import json
import logging
from typing import List

import src.external_api as external_api

logger = logging.getLogger(__name__)
logger.setLevel(logging.DEBUG)
file_handler = logging.FileHandler('logs/utils.log', mode='w')
file_formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s: %(message)s')
file_handler.setFormatter(file_formatter)
logger.addHandler(file_handler)


def load_transactions(file_path: str) -> List[dict]:
    """
    Загружает данные о финансовых транзакциях из указанного JSON-файла.
    Возвращает список словарей с данными транзакций.
    Если файл отсутствует, пуст или содержит неверные данные,
    возвращается пустой список.

    :param file_path: Путь до JSON-файла
    :return: Список словарей с данными транзакций
    """
    logger.debug(f'Начало загрузки транзакций из файла: {file_path}')
    
    try:
        logger.debug('Попытка открыть файл')
        with open(file_path, encoding="utf-8") as file:
            logger.debug('Файл открыт, начинаем парсинг JSON')
            data = json.load(file)
            logger.debug(f'JSON успешно распарсен, тип данных: {type(data)}')

        # Проверяем, что файл содержит именно список объектов
        if isinstance(data, list):
            logger.debug(f'Файл содержит список из {len(data)} элементов')
            logger.info("Файл содержит именно список объектов")
            return data
        else:
            logger.debug(f'Файл содержит не список, а {type(data)}')
            logger.error("Файл не содержит список объектов")
            return []
    except FileNotFoundError:
        logger.debug(f'Файл не найден по пути: {file_path}')
        logger.error(f"Файл не найден: {file_path}")
        return []
    except json.JSONDecodeError as e:
        logger.debug(f'Ошибка парсинга JSON: {str(e)}')
        logger.error(f"Ошибка в структуре JSON файла: {file_path}")
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
    logger.debug(f'Начало обработки транзакции: {transaction.get("id", "unknown")}')
    
    amount = transaction["operationAmount"]["amount"]
    currency = transaction["operationAmount"]["currency"]["code"].upper()
    
    logger.debug(f'Сумма транзакции: {amount}, валюта: {currency}')

    if currency == "RUB":
        logger.debug('Валюта RUB, конвертация не требуется')
        return float(amount)
    else:
        logger.debug(f'Валюта {currency}, требуется конвертация в RUB')
        converted_amount = float(external_api.convert_currency(amount, currency))
        logger.debug(f'Конвертированная сумма: {converted_amount}')
        return converted_amount
