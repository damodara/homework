from unittest.mock import patch

import pytest

from src.external_api import convert_currency
from src.utils import load_transactions, process_transaction


# Тестирование load_transactions
# Тестируем загрузку корректного файла JSON
def test_load_valid_json_file(tmpdir):
    # Создаем временной файл с данными
    temp_file = tmpdir.join("valid_operations.json")
    valid_data = '[{"id": 1, "amount": 100}]'
    temp_file.write(valid_data)

    result = load_transactions(str(temp_file))
    assert len(result) == 1
    assert result[0]["id"] == 1
    assert result[0]["amount"] == 100


# Тестируем обработку пустого файла
def test_load_empty_file(tmpdir):
    temp_file = tmpdir.join("empty.json")
    empty_data = ""
    temp_file.write(empty_data)

    result = load_transactions(str(temp_file))
    assert result == []


# Тестируем обработку неправильного формата JSON
def test_load_invalid_json_file(tmpdir):
    temp_file = tmpdir.join("invalid.json")
    invalid_data = '{"id": 1, "amount"}'  # Неправильный JSON
    temp_file.write(invalid_data)

    result = load_transactions(str(temp_file))
    assert result == []


# Тестируем обработку несуществующего файла
def test_load_nonexistent_file() -> None:
    non_existent_file = "/path/to/nonexistent/file.json"
    result = load_transactions(non_existent_file)
    assert result == []


# Тестирование process_transaction
# Тестируем транзакцию в рублях
def test_process_transaction_rub() -> None:
    transaction = {"operationAmount": {"amount": 100.0, "currency": {"code": "RUB"}}}
    result = process_transaction(transaction)
    assert result == 100.0


# Тестируем транзакцию в иностранной валюте с моком для convert_currency
@patch("src.external_api.convert_currency")
def test_process_transaction_foreign_currency(mock_convert):
    transaction = {"operationAmount": {"amount": 100.0, "currency": {"code": "USD"}}}
    mock_convert.return_value = 6500.0  # Смоделированное значение после конвертации

    result = process_transaction(transaction)
    assert result == 6500.0
    mock_convert.assert_called_once_with(100.0, "USD")


# Тестируем транзакцию с исключением при ошибочной валюте
def test_process_transaction_missing_fields() -> None:
    transaction = {"operationAmount": {"amount": 100.0}}
    with pytest.raises(KeyError):
        process_transaction(transaction)
