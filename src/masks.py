from src.decorators import log


@log(filename="mylog.txt")
def get_mask_card_number(card_number: str) -> str:
    """Функция принимает на вход номер карты и возвращает ее маску
    7000792289606361        входной аргумент
    7000 79** **** 6361     выход функции
    """
    if len(card_number) != 16 or not card_number.isdigit():
        return "Номер карты должен быть строкой из 16 цифр"
    else:
        block1 = card_number[:4]
        block2 = card_number[4:6] + "**"
        block3 = "****"
        block4 = card_number[12:16]
        masked_number = f"{block1} {block2} {block3} {block4}"
        return masked_number


@log(filename="mylog.txt")
def get_mask_account(account_number: str) -> str:
    """Функция принимает на вход номер счета и возвращает его маску
    73654108430135874305     входной аргумент
    **4305                   выход функции
    """
    if len(account_number) != 20 or not account_number.isdigit():
        return "Номер счета должен быть строкой из 20 цифр"
    else:
        return "**" + account_number[-4:]
