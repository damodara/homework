from src.processing import filter_by_state, sort_by_date


def test_filter_by_state(test_data: list) -> None:
    """Тестируем фильтр по состоянию операции"""
    expected_result = [
        {"id": 1, "state": "EXECUTED", "date": "2023-08-01T12:00:00"},
        {"id": 3, "state": "EXECUTED", "date": "2023-08-02T13:00:00"},
    ]
    result = filter_by_state(test_data)
    assert result == expected_result


def test_sort_by_date(test_data: list) -> None:
    """Проверяем сортировку по дате"""
    expected_result = [
        {"id": 3, "state": "EXECUTED", "date": "2023-08-02T13:00:00"},
        {"id": 1, "state": "EXECUTED", "date": "2023-08-01T12:00:00"},
        {"id": 2, "state": "CANCELED", "date": "2023-07-31T11:00:00"},
    ]
    result = sort_by_date(test_data)
    assert result == expected_result


def test_filter_by_state_with_canceled(test_data: list) -> None:
    """Дополнительно проверим работу фильтрации с другим состоянием"""
    expected_result = [{"id": 2, "state": "CANCELED", "date": "2023-07-31T11:00:00"}]
    result = filter_by_state(test_data, state="CANCELED")
    assert result == expected_result
