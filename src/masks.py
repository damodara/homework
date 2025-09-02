from src.decorators import log
import logging

logger = logging.getLogger(__name__)
logger.setLevel(logging.DEBUG)
file_handler = logging.FileHandler('logs/masks.log', mode='w')
file_formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s: %(message)s')
file_handler.setFormatter(file_formatter)
logger.addHandler(file_handler)


@log(filename="mylog.txt")
def get_mask_card_number(card_number: str) -> str:
    """Функция принимает на вход номер карты и возвращает ее маску
    7000792289606361        входной аргумент
    7000 79** **** 6361     выход функции
    """
    logger.info(f'Функция get_mask_card_number принимает номер карты {card_number}')
    if len(card_number) != 16 or not card_number.isdigit():
        logger.error(f'Введен неверный формат номера карты: {card_number}')
        return "Номер карты должен быть строкой из 16 цифр"
    else:
        block1 = card_number[:4]
        block2 = card_number[4:6] + "**"
        block3 = "****"
        block4 = card_number[12:16]
        masked_number = f"{block1} {block2} {block3} {block4}"
        logger.info(f'Получили маску из номера: {masked_number}')
        return masked_number


@log(filename="mylog.txt")
def get_mask_account(account_number: str) -> str:
    """Функция принимает на вход номер счета и возвращает его маску
    73654108430135874305     входной аргумент
    **4305                   выход функции
    """
    logger.info(f'Функция get_mask_account принимает номер счета {account_number}')
    if len(account_number) != 20 or not account_number.isdigit():
        logger.error(f'Введен неверный формат номера счета: {account_number}')
        return "Номер счета должен быть строкой из 20 цифр"
    else:
        masked_account = "**" + account_number[-4:]
        logger.info(f'Получили маску из номера счета: {masked_account}')
        return masked_account
