from typing import Any, Dict, Generator


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
