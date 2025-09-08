import json

from src.operations_loader import read_operations
from src.processing import filter_by_state, process_bank_search, sort_by_date
from src.utils import load_transactions
from src.widget import get_date, mask_account_card


def _prompt_choice(prompt: str, choices: list[str]) -> str:
    while True:
        value = input(prompt).strip()
        if value.lower() in [c.lower() for c in choices]:
            # вернуть в оригинальном регистре из choices
            for c in choices:
                if value.lower() == c.lower():
                    return c
        print(f"Недопустимое значение: {value}")


def main() -> None:
    print("Привет! Добро пожаловать в программу работы с банковскими транзакциями.")
    print("Выберите необходимый пункт меню:")
    print("1. Получить информацию о транзакциях из JSON-файла")
    print("2. Получить информацию о транзакциях из CSV-файла")
    print("3. Получить информацию о транзакциях из XLSX-файла")

    source = input().strip()
    data: list[dict]
    if source == "1":
        print("Для обработки выбран JSON-файл.")
        path = input("Укажите путь к JSON-файлу: ").strip()
        data = load_transactions(path)
    elif source == "2":
        print("Для обработки выбран CSV-файл.")
        path = input("Укажите путь к CSV-файлу: ").strip()
        data = read_operations(path)
    elif source == "3":
        print("Для обработки выбран XLSX-файл.")
        path = input("Укажите путь к XLSX-файлу: ").strip()
        data = read_operations(path)
    else:
        print("Неизвестный пункт меню")
        return

    # Ввод статуса
    allowed_statuses = ["EXECUTED", "CANCELED", "PENDING"]
    while True:
        print("Введите статус, по которому необходимо выполнить фильтрацию.")
        print("Доступные для фильтровки статусы: EXECUTED, CANCELED, PENDING")
        status_input = input().strip().upper()
        if status_input in allowed_statuses:
            print(f'Операции отфильтрованы по статусу "{status_input}"')
            break
        else:
            print(f'Статус операции "{status_input}" недоступен.')

    # Фильтрация по статусу
    filtered = [op for op in data if str(op.get("state", "")).upper() == status_input]

    # Сортировка по дате
    sort_answer = _prompt_choice("Отсортировать операции по дате? Да/Нет\n", ["Да", "Нет"])
    if sort_answer.lower() == "да":
        order = _prompt_choice("Отсортировать по возрастанию или по убыванию?\n", ["по возрастанию", "по убыванию"])
        reverse = order == "по убыванию"
        # Используем готовую функцию sort_by_date
        try:
            filtered = sort_by_date(filtered, reverse=reverse)
        except Exception:
            pass

    # Только рублевые
    rub_only = _prompt_choice("Выводить только рублевые транзакции? Да/Нет\n", ["Да", "Нет"]).lower() == "да"
    if rub_only:
        filtered = [
            op for op in filtered if op.get("operationAmount", {}).get("currency", {}).get("code", "").upper() == "RUB"
        ]

    # Фильтр по слову в описании
    search_answer = _prompt_choice(
        "Отфильтровать список транзакций по определенному слову в описании? Да/Нет\n", ["Да", "Нет"]
    ).lower()
    if search_answer == "да":
        term = input("Введите слово/фразу для поиска: ").strip()
        filtered = process_bank_search(filtered, term)

    # Вывод результата
    print("Распечатываю итоговый список транзакций...")
    print(f"Всего банковских операций в выборке: {len(filtered)}")
    if not filtered:
        print("Не найдено ни одной транзакции, подходящей под ваши условия фильтрации")
        return

    for op in filtered:
        date_str = op.get("date", "")
        try:
            date_out = get_date(date_str)
        except Exception:
            date_out = date_str
        desc = op.get("description", "")
        from_str = op.get("from", "")
        to_str = op.get("to", "")
        amount = op.get("operationAmount", {}).get("amount", "")
        code = op.get("operationAmount", {}).get("currency", {}).get("code", "")

        line_from = mask_account_card(from_str) if from_str else ""
        line_to = mask_account_card(to_str) if to_str else ""

        print()
        print(f"{date_out} {desc}")
        if line_from or line_to:
            arrow = f"{line_from} -> {line_to}" if line_from and line_to else line_from or line_to
            print(arrow)
        print(f"Сумма: {amount} {code}")


if __name__ == "__main__":
    main()
