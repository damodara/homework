from src.masks import get_mask_account, get_mask_card_number


def mask_account_card(card_data: str) -> str:
    """функция обрабатывает информацию как о картах, так и о счетах
            # Пример для карты
        Visa Platinum 7000792289606361  # входной аргумент
        Visa Platinum 7000 79** **** 6361  # выход функции

            # Пример для счета
        Счет 73654108430135874305  # входной аргумент
        Счет **4305  # выход функции
        """
    name, number = card_data.rsplit(' ', maxsplit=1)

    if name.lower() == 'счет':
        masked_number = get_mask_account(number)
        if isinstance(masked_number, str) and masked_number.startswith("Номер"):  # Если возникла ошибка
            return masked_number
    else:
        masked_number = get_mask_card_number(number)
        if isinstance(masked_number, str) and masked_number.startswith("Номер"):  # Если возникла ошибка
            return masked_number

    return f'{name} {masked_number}'


def get_date(date: str) -> str:
    """функция меняет формат даты.
    Принимает на вход строку с датой в формате
    "2024-03-11T02:26:18.671407"
    и возвращает строку с датой в формате
    "ДД.ММ.ГГГГ"("11.03.2024")
    """
    if len(date) < 19:  # Дата должна содержать минимум 19 символов (формат YYYY-MM-DDTHH:mm:ss.SSSSSS)
        return "Недопустимый формат даты"

    year = date[:4]
    month = date[5:7]
    day = date[8:10]
    return f"{day}.{month}.{year}"
