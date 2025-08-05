from src.masks import get_mask_account, get_mask_card_number


def test_get_mask_card_number_correct_type() -> None:
    assert get_mask_card_number("7000792289606361") == "7000 79** **** 6361"


def test_get_mask_card_number_lenth() -> None:
    assert get_mask_card_number("123456789012345") == "Номер карты должен быть строкой из 16 цифр"
    assert get_mask_card_number("12345678901234567") == "Номер карты должен быть строкой из 16 цифр"


def test_get_mask_card_number_isdigit() -> None:
    assert get_mask_card_number("abcde1234567890") == "Номер карты должен быть строкой из 16 цифр"
    assert get_mask_card_number("!@#$%^&*()_+") == "Номер карты должен быть строкой из 16 цифр"


def test_get_mask_card_number_empty() -> None:
    assert get_mask_card_number("") == "Номер карты должен быть строкой из 16 цифр"


def test_get_mask_account_correct_type() -> None:
    assert get_mask_account("73654108430135874305") == "**4305"


def test_get_mask_account_correct_lenth() -> None:
    assert get_mask_account("1234567890123456789") == "Номер счета должен быть строкой из 20 цифр"
    assert get_mask_account("123456789012345678901") == "Номер счета должен быть строкой из 20 цифр"


def test_get_mask_account_correct_isdigit() -> None:
    assert get_mask_account("abcde1234567890") == "Номер счета должен быть строкой из 20 цифр"
    assert get_mask_account("!@#$%^&*()_+") == "Номер счета должен быть строкой из 20 цифр"
