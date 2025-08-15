from typing import Any, Dict, List

import pytest

from src.generators import card_number_generator, filter_by_currency, transaction_descriptions


@pytest.mark.parametrize(
    "currency_code, expected_count",
    [
        ("USD", 3),
        ("EUR", 0),
        ("JPY", 0),
        ("RUB", 2),
    ],
)
def test_filter_by_currency_parametrized(
    sample_transactions: List[Dict[str, Any]], currency_code: str, expected_count: int
) -> None:
    """Тестирование фильтрации по различным валютам."""
    filtered_transactions = list(filter_by_currency(sample_transactions, currency_code))
    assert len(filtered_transactions) == expected_count


@pytest.mark.parametrize(
    "start_position, end_position, expected_numbers",
    [
        (
            1,
            5,
            [
                "0000 0000 0000 0001",
                "0000 0000 0000 0002",
                "0000 0000 0000 0003",
                "0000 0000 0000 0004",
                "0000 0000 0000 0005",
            ],
        ),
        (
            1000,
            1005,
            [
                "0000 0000 0000 1000",
                "0000 0000 0000 1001",
                "0000 0000 0000 1002",
                "0000 0000 0000 1003",
                "0000 0000 0000 1004",
                "0000 0000 0000 1005",
            ],
        ),
        (1, 1, ["0000 0000 0000 0001"]),
        (5, 1, []),
        (9999999999999999, 9999999999999999, ["9999 9999 9999 9999"]),
    ],
)
def test_card_number_generator_parametrized(
    start_position: int, end_position: int, expected_numbers: List[str]
) -> None:
    """Тестируем генерацию номеров карт для различных диапазонов."""
    generated_numbers = list(card_number_generator(start_position, end_position))
    assert generated_numbers == expected_numbers


def test_transaction_descriptions(sample_transactions: List[Dict[str, Any]]) -> None:
    """Тестируем получение описаний транзакций."""
    descriptions = list(transaction_descriptions(sample_transactions))
    expected_descriptions = [
        "Перевод организации",
        "Перевод со счета на счет",
        "Перевод со счета на счет",
        "Перевод с карты на карту",
        "Перевод организации",
    ]
    assert descriptions == expected_descriptions


def test_empty_transactions() -> None:
    """Тестируем передачу пустого списка транзакций."""
    empty_transactions: List[Dict[str, Any]] = []
    descriptions = list(transaction_descriptions(empty_transactions))
    assert descriptions == [], "Должен вернуть пустой список для пустых транзакций"


def test_single_transaction() -> None:
    """Тестируем единственный элемент транзакции."""
    single_transaction = [{"id": 1, "description": "Отправка средств"}]
    descriptions = list(transaction_descriptions(single_transaction))
    assert descriptions == ["Отправка средств"], "Описание должно соответствовать единственной транзакции"


def test_missing_description_key() -> None:
    """Тестируем отсутствие ключа description."""
    transactions_without_description: List[Dict[str, Any]] = [{"id": 1}, {"id": 2, "description": "Покупка билета"}]
    with pytest.raises(KeyError):
        next(transaction_descriptions(transactions_without_description))
