def filter_by_currency(transactions: list, currency_code: str) -> dict:
    """Функция должна возвращать итератор, который поочередно выдает транзакции, где валюта операции соответствует
    заданной"""
    return (
        transaction for transaction in transactions
        if transaction.get("operationAmount", {}).get("currency", {}).get("code") == currency_code
    )

