from typing import Any, Dict, Generator, List


def filter_by_currency(
    transactions: list[Dict[str, Any]], currency_code: str
) -> Generator[Dict[str, Any], None, None]:
    """
    Возвращает итератор, выдающий транзакции, соответствующие указанной валюте.

    :param transactions: Список словарей, каждый представляет отдельную транзакцию.
    :param currency_code: Код валюты (например, "USD").
    :return: Итератор, выдающий подходящие транзакции.
    """
    return (
        transaction
        for transaction in transactions
        if transaction.get("operationAmount", {}).get("currency", {}).get("code") == currency_code
    )


def transaction_descriptions(transactions: List[Dict[str, Any]]) -> Generator[str, None, None]:
    """
    Возвращает описание каждой операции по очереди

    :param transactions: Список словарей, каждый представляет отдельную транзакцию.
    :return: Описание каждой операции по очереди
    """
    for transaction in transactions:
        yield transaction["description"]


def card_number_generator(start_position: int, end_position: int) -> Generator[str, None, None]:
    """
    Генератор должен принимать начальное и конечное значения для генерации диапазона номеров
    Генератор может сгенерировать номера карт в заданном диапазоне от 0000 0000 0000 0001 до 9999 9999 9999 9999

    :param start_position: Начальное число для генератора
    :param end_position: Конечное число для генератора
    :return: выдает номера банковских карт в формате XXXX XXXX XXXX XXXX
    """
    for number in range(start_position, end_position + 1):
        formatted_card_number = f"{number:016d}"
        result = " ".join(formatted_card_number[i : i + 4] for i in range(0, len(formatted_card_number), 4))
        yield result
