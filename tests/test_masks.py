from src.masks import get_mask_account, get_mask_card_number

from .conftest import invalid_account_numbers, invalid_card_numbers, valid_account_number, valid_card_number


def test_get_mask_card_number_correct_type(valid_card_number: str) -> None:
    expected_result = "7000 79** **** 6361"
    result = get_mask_card_number(valid_card_number)
    assert result == expected_result


def test_get_mask_card_number_length(invalid_card_numbers: list) -> None:
    for number in invalid_card_numbers:
        result = get_mask_card_number(number)
        assert result == "Номер карты должен быть строкой из 16 цифр"


def test_get_mask_account_correct_type(valid_account_number: str) -> None:
    expected_result = "**4305"
    result = get_mask_account(valid_account_number)
    assert result == expected_result


def test_get_mask_account_length(invalid_account_numbers: list) -> None:
    for number in invalid_account_numbers:
        result = get_mask_account(number)
        assert result == "Номер счета должен быть строкой из 20 цифр"
