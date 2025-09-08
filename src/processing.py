import re
from collections import Counter
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


def process_bank_search(data: list[dict], search: str) -> list[dict]:
    """Возвращает список операций, в описании которых встречается строка поиска."""
    if not search:
        return []

    pattern = re.compile(re.escape(search), flags=re.IGNORECASE)
    result: list[dict] = []
    for operation in data:
        description = operation.get("description", "")
        if isinstance(description, str) and pattern.search(description):
            result.append(operation)
    return result


def process_bank_operations(data: list[dict], categories: list[str]) -> dict[str, int]:
    """Возвращает словарь: категория -> количество операций по ней."""
    category_patterns: dict[str, re.Pattern[str]] = {
        category: re.compile(re.escape(category), flags=re.IGNORECASE) for category in categories
    }

    counter: Counter[str] = Counter()

    for item in data:
        description = item.get("description", "")
        if not isinstance(description, str):
            continue
        for category, pattern in category_patterns.items():
            if pattern.search(description):
                counter[category] += 1

    result: dict[str, int] = {category: counter.get(category, 0) for category in categories}
    return result
