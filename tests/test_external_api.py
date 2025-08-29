import os
from unittest.mock import Mock, patch

import pytest

from src.external_api import convert_currency


# Тест успешного конвертирования валюты
@patch("src.external_api.requests.get")
def test_convert_currency_success(mock_get):
    # Подготавливаем фиктивный ответ от API
    mock_response = Mock()
    mock_response.json.return_value = {"result": 123.45}
    mock_response.raise_for_status = Mock()
    mock_get.return_value = mock_response

    # Запустим функцию с необходимыми параметрами
    amount = 100
    from_currency = "USD"
    to_currency = "RUB"

    result = convert_currency(amount, from_currency, to_currency)

    # Проверим, что функция вернула правильный результат
    assert result == 123.45

    # Проверим, что requests.get был вызван с правильными параметрами
    # expected_url = f"https://api.apilayer.com/exchangerates_data/convert?to={to_currency}&from={from_currency}&amount={amount}"
    # mock_get.assert_called_once_with(expected_url, headers={"apikey": os.getenv('API_KEY')})


# Тест на обработку ошибки API
@patch("src.external_api.requests.get")
def test_convert_currency_api_error(mock_get):
    # Моделируем ошибку API
    mock_response = Mock()
    mock_response.raise_for_status.side_effect = Exception("API error")
    mock_get.return_value = mock_response

    # Запустим функцию и поймаем исключение
    with pytest.raises(Exception) as excinfo:
        convert_currency(100, "USD", "RUB")

    # Проверим, что исключение содержит нужную информацию
    assert "API error" in str(excinfo.value)


# Тест по умолчанию валюты (to_currency='RUB')
@patch("src.external_api.requests.get")
def test_convert_currency_default_to_currency(mock_get):
    # Подготовим фиктивный ответ от API
    mock_response = Mock()
    mock_response.json.return_value = {"result": 200}
    mock_response.raise_for_status = Mock()
    mock_get.return_value = mock_response

    # Запустим функцию с одним параметром
    result = convert_currency(50, "EUR")

    # Проверим, что результат правильный
    assert result == 200

    # Проверим, что requests.get был вызван с правильными параметрами
    expected_url = "https://api.apilayer.com/exchangerates_data/convert?to=RUB&from=EUR&amount=50"
    mock_get.assert_called_once_with(expected_url, headers={"apikey": os.getenv("API_KEY")})
