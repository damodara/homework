from datetime import datetime

from src.decorators import log


@log(filename="mylog.txt")
def filter_by_state(data_list: list, state: str = "EXECUTED") -> list:
    """Функция возвращает новый список словарей, содержащий только те словари, у которых ключ
    state соответствует указанному значению"""
    filtered_list = []
    for item in data_list:
        if item.get("state") == state:
            filtered_list.append(item)
    return filtered_list


def sort_by_date(data_list: list, reverse: bool = True) -> list:
    """Функция должна возвращать новый список, отсортированный по дате"""
    return sorted(data_list, key=lambda x: datetime.fromisoformat(x["date"]), reverse=reverse)
