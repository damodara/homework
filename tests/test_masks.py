from src.masks import get_mask_account, get_mask_card_number


def test_get_mask_card_number() -> None:
    assert get_mask_card_number("7000792289606361") == "7000 79** **** 6361"


def test_get_mask_card_number_lenth() -> None:
    assert get_mask_card_number("123456789012345") == "Номер карты должен быть строкой из 16 цифр"
    assert get_mask_card_number("12345678901234567") == "Номер карты должен быть строкой из 16 цифр"


def test_get_mask_card_number_isdigit() -> None:
    assert get_mask_card_number("abcde1234567890") == "Номер карты должен быть строкой из 16 цифр"
    assert get_mask_card_number("!@#$%^&*()_+") == "Номер карты должен быть строкой из 16 цифр"


def test_get_mask_card_number_empty() -> None:
    assert get_mask_card_number("") == "Номер карты должен быть строкой из 16 цифр"
