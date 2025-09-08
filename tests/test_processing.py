import pytest

from src.processing import filter_by_state, process_bank_operations, process_bank_search, sort_by_date
from tests.conftest import (
    data_for_filter_by_state_with_canceled,
    data_for_sort_by_date,
    data_of_filter_by_state,
    test_data,
)


@pytest.mark.parametrize("data", data_of_filter_by_state)
def test_filter_by_state(test_data: list, data: dict) -> None:
    """Тестируем фильтр по состоянию операции"""
    state = data["state"]
    expected_result = data["expected_result"]
    result = filter_by_state(test_data, state)
    assert result == expected_result


@pytest.mark.parametrize("data", data_for_sort_by_date)
def test_sort_by_date(test_data: list, data: dict) -> None:
    """Проверяем сортировку по дате"""
    reverse = data["reverse"]
    expected_result = data["expected_result"]
    result = sort_by_date(test_data, reverse=reverse)
    assert result == expected_result


@pytest.mark.parametrize("data", data_for_filter_by_state_with_canceled)
def test_filter_by_state_with_canceled(test_data: list, data: dict) -> None:
    """Дополнительная проверка фильтрации по состоянию CANCELED"""
    state = data["state"]
    expected_result = data["expected_result"]
    result = filter_by_state(test_data, state)
    assert result == expected_result


def test_process_bank_search_basic() -> None:
    data = [
        {"description": "Перевод организации", "id": 1},
        {"description": "Оплата услуг", "id": 2},
        {"description": "перевод со счета на счет", "id": 3},
        {"description": None, "id": 4},
    ]

    # Регистронезависимый поиск по подстроке
    result = process_bank_search(data, "Перевод")
    ids = [item["id"] for item in result]
    assert ids == [1, 3]

    # Пустая строка поиска -> пустой список
    assert process_bank_search(data, "") == []


def test_process_bank_operations_counts() -> None:
    data = [
        {"description": "Перевод организации"},
        {"description": "Оплата услуг мобильной связи"},
        {"description": "ПЕРЕВОД СО СЧЕТА НА СЧЕТ"},
        {"description": "Перевод с карты на карту"},
        {"description": "Неизвестная операция"},
        {"description": None},
    ]
    categories = ["Перевод", "Оплата", "Пополнение"]

    counts = process_bank_operations(data, categories)
    assert counts == {"Перевод": 3, "Оплата": 1, "Пополнение": 0}
