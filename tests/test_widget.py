from src.widget import get_date, mask_account_card

from .conftest import invalid_data, invalid_dates, valid_data, valid_dates


def test_valid_data(valid_data: list) -> None:
    """Проверка на корректные данные"""
    for input_data, expected_output in valid_data:
        result = mask_account_card(input_data)
        assert (
            result == expected_output
        ), f"Ошибка при проверке данных: {input_data}, ожидался вывод: {expected_output}, фактически: {result}"


def test_invalid_data(invalid_data: list) -> None:
    """Проверка на некорректные данные"""
    for input_data, expected_error_message in invalid_data:
        result = mask_account_card(input_data)
        assert (
            result == expected_error_message
        ), f"Ошибка при проверке данных: {input_data}, ожидалась ошибка: {expected_error_message}, фактически: {result}"


def test_valid_dates(valid_dates: list) -> None:
    """Проверка корректности преобразованных дат"""
    for input_date, expected_output in valid_dates:
        result = get_date(input_date)
        assert (
            result == expected_output
        ), f"Ошибка при проверке даты: {input_date}, ожидался вывод: {expected_output}, фактически: {result}"


def test_invalid_dates(invalid_dates: list) -> None:
    """Проверка некорректных дат"""
    for input_date, expected_error_message in invalid_dates:
        result = get_date(input_date)
        assert (
            result == expected_error_message
        ), f"Ошибка при проверке даты: {input_date}, ожидалась ошибка: {expected_error_message}, фактически: {result}"
