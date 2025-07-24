def filter_by_state(data_list: list, state = "EXECUTED") -> list:
    """Функция возвращает новый список словарей, содержащий только те словари, у которых ключ
state соответствует указанному значению"""
    filtered_list = []
    for item in data_list:
        if item.get("state") == state:
            filtered_list.append(item)
    return filtered_list
