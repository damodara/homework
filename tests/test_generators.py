from typing import Any, Dict, List

import pytest

from src.generators import card_number_generator, filter_by_currency, transaction_descriptions


def test_filter_usd(sample_transactions: List[Dict[str, Any]]) -> None:
    """Тестирование фильтрации по валюте USD."""
    usd_transactions = list(filter_by_currency(sample_transactions, "USD"))
    assert len(usd_transactions) == 3
    assert all(transaction["operationAmount"]["currency"]["code"] == "USD" for transaction in usd_transactions)


def test_no_matches(sample_transactions: List[Dict[str, Any]]) -> None:
    """Тестирование случая, когда нет подходящих транзакций."""
    jpy_transactions = list(filter_by_currency(sample_transactions, "JPY"))
    assert jpy_transactions == []


def test_mixed_currencies(sample_transactions: List[Dict[str, Any]]) -> None:
    """Тестирование смешанного набора валют."""
    eur_transactions = list(filter_by_currency(sample_transactions, "EUR"))
    assert len(eur_transactions) == 0


def test_missing_fields(sample_transactions: List[Dict[str, Any]]) -> None:
    """Тестирование пропуска некоторых ключевых полей."""
    missing_field_transactions = list(filter_by_currency([{"id": 7}], "USD"))
    assert missing_field_transactions == []


def test_empty_list() -> None:
    """Тестирование пустой передачи списка транзакций."""
    empty_transactions = list(filter_by_currency([], "USD"))
    assert empty_transactions == []


def test_transaction_descriptions(sample_transactions: List[Dict[str, Any]]) -> None:
    """Тестируем получение описаний транзакций"""
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
    """Тестируем передачу пустого списка транзакций"""
    empty_transactions: List[Dict[str, Any]] = []
    descriptions = list(transaction_descriptions(empty_transactions))
    assert descriptions == [], "Должен вернуть пустой список для пустых транзакций"


def test_single_transaction() -> None:
    """Тестируем единственный элемент транзакции"""
    single_transaction = [{"id": 1, "description": "Отправка средств"}]
    descriptions = list(transaction_descriptions(single_transaction))
    assert descriptions == ["Отправка средств"], "Описание должно соответствовать единственной транзакции"


def test_missing_description_key() -> None:
    """Тестируем отсутствие ключа description"""
    transactions_without_description: List[Dict[str, Any]] = [{"id": 1}, {"id": 2, "description": "Покупка билета"}]
    with pytest.raises(KeyError):
        next(transaction_descriptions(transactions_without_description))


def test_card_number_generator_range() -> None:
    """Тестирует генерацию последовательности номеров карт в заданном диапазоне."""
    generator = card_number_generator(1, 5)
    generated_numbers = list(generator)
    expected_result = [
        "0000 0000 0000 0001",
        "0000 0000 0000 0002",
        "0000 0000 0000 0003",
        "0000 0000 0000 0004",
        "0000 0000 0000 0005",
    ]
    assert generated_numbers == expected_result


def test_large_range() -> None:
    """Тестирует генерацию большого количества номеров карт."""
    generator = card_number_generator(1000, 1005)
    generated_numbers = list(generator)
    expected_result = [
        "0000 0000 0000 1000",
        "0000 0000 0000 1001",
        "0000 0000 0000 1002",
        "0000 0000 0000 1003",
        "0000 0000 0000 1004",
        "0000 0000 0000 1005",
    ]
    assert generated_numbers == expected_result


def test_start_and_end_are_equal() -> None:
    """Тестирует случай, когда старт и финиш одинаковы."""
    generator = card_number_generator(1, 1)
    generated_numbers = list(generator)
    expected_result = ["0000 0000 0000 0001"]
    assert generated_numbers == expected_result


def test_empty_range() -> None:
    """Тестирует случай, когда диапазон пуст (начало больше конца)."""
    generator = card_number_generator(5, 1)
    generated_numbers = list(generator)
    expected_result: List[str] = []
    assert generated_numbers == expected_result


def test_max_range() -> None:
    """Тестирует крайний случай: генерация максимального номера карты."""
    generator = card_number_generator(9999999999999999, 9999999999999999)
    generated_numbers = list(generator)
    expected_result = ["9999 9999 9999 9999"]
    assert generated_numbers == expected_result
