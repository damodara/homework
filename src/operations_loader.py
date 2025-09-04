import os
from typing import Dict, List

import pandas as pd


def read_csv(path: str) -> List[Dict]:
    """
    Читает CSV
    :param path: Указываем название файла
    :return: Функция возвращает список словарей (records).
    """
    try:
        df = pd.read_csv(path)
    except FileNotFoundError as e:
        raise FileNotFoundError(f"CSV-файл не найден: {path}") from e
    except Exception as e:
        raise RuntimeError(f"Ошибка чтения CSV: {path}") from e
    return df.to_dict(orient="records")


def read_xlsx(path: str) -> List[Dict]:
    """
    Читает XLS/XLSX.
    :param path: Указываем название файла
    :return: Функция возвращает список словарей (records).
    """
    try:
        df = pd.read_excel(path)
    except FileNotFoundError as e:
        raise FileNotFoundError(f"XLSX-файл не найден: {path}") from e
    except Exception as e:
        raise RuntimeError(f"Ошибка чтения XLS/XLSX: {path}") from e
    return df.to_dict(orient="records")


def read_operations(path: str) -> List[Dict]:
    """Определяет формат по расширению и читает операции."""
    ext = os.path.splitext(path)[1].lower()
    if ext == ".csv":
        return read_csv(path)
    if ext in (".xlsx", ".xls"):
        return read_xlsx(path)
    raise ValueError(f"Неизвестный формат файла: {ext}")
