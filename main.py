from src.widget import get_date, mask_account_card


def main() -> None:
    """Основная функция для проверки"""
    values = [
        "Maestro 1596837868705199",
        "Счет 64686473678894779589",
        "MasterCard 7158300734726758",
        "Счет 35383033474447895560",
        "Visa Classic 6831982476737658",
        "Visa Platinum 8990922113665229",
        "Visa Gold 5999414228426353",
        "Счет 73654108430135874305",
    ]
    date = "2018-07-11T02:26:18.671407"

    for value in values:
        print(mask_account_card(value))

    print(get_date(date))


if __name__ == "__main__":
    main()
