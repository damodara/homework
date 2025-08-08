import pytest

from src.processing import filter_by_state, sort_by_date
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
