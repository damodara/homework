import pytest


@pytest.fixture
def test_data() -> list:
    return [
        {"id": 1, "state": "EXECUTED", "date": "2023-08-01T12:00:00"},
        {"id": 2, "state": "CANCELED", "date": "2023-07-31T11:00:00"},
        {"id": 3, "state": "EXECUTED", "date": "2023-08-02T13:00:00"},
    ]


# Параметры для фильтрации по различным состояниям
data_of_filter_by_state = [
    {
        "state": "EXECUTED",
        "expected_result": [
            {"id": 1, "state": "EXECUTED", "date": "2023-08-01T12:00:00"},
            {"id": 3, "state": "EXECUTED", "date": "2023-08-02T13:00:00"},
        ],
    },
    {"state": "CANCELED", "expected_result": [{"id": 2, "state": "CANCELED", "date": "2023-07-31T11:00:00"}]},
]

# Параметры для сортировки по дате
data_for_sort_by_date = [
    {
        "reverse": True,
        "expected_result": [
            {"id": 3, "state": "EXECUTED", "date": "2023-08-02T13:00:00"},
            {"id": 1, "state": "EXECUTED", "date": "2023-08-01T12:00:00"},
            {"id": 2, "state": "CANCELED", "date": "2023-07-31T11:00:00"},
        ],
    },
    {
        "reverse": False,
        "expected_result": [
            {"id": 2, "state": "CANCELED", "date": "2023-07-31T11:00:00"},
            {"id": 1, "state": "EXECUTED", "date": "2023-08-01T12:00:00"},
            {"id": 3, "state": "EXECUTED", "date": "2023-08-02T13:00:00"},
        ],
    },
]

# Параметры для фильтрации по CANCELED
data_for_filter_by_state_with_canceled = [
    {"state": "CANCELED", "expected_result": [{"id": 2, "state": "CANCELED", "date": "2023-07-31T11:00:00"}]}
]


@pytest.fixture
def valid_card_number() -> str:
    # Возвращаем правильный номер карты
    return "7000792289606361"


@pytest.fixture
def invalid_card_numbers() -> list:
    # Список неправильных номеров карт для проверки ошибок
    return ["123456789012345", "12345678901234567", "abcde1234567890", "!@#$%^&*()_+", ""]


@pytest.fixture
def valid_account_number() -> str:
    # Возвращаем правильный номер счёта
    return "73654108430135874305"


@pytest.fixture
def invalid_account_numbers() -> list:
    # Список неправильных номеров счетов для проверки ошибок
    return ["1234567890123456789", "123456789012345678901", "abcde1234567890", "!@#$%^&*()_+", ""]


@pytest.fixture
def valid_data() -> list:
    # Валидные данные для успешной обработки
    return [
        ("Visa Platinum 7000792289606361", "Visa Platinum 7000 79** **** 6361"),
        ("MasterCard Gold 5469241538462379", "MasterCard Gold 5469 24** **** 2379"),
        ("Счет 73654108430135874305", "Счет **4305"),
        ("Maestro Standard 1234567890123456", "Maestro Standard 1234 56** **** 3456"),
    ]


@pytest.fixture
def invalid_data() -> list:
    # Инвалидые данные для проверки обработки ошибок
    return [
        ("Visa Platinum 123456789012345", "Номер карты должен быть строкой из 16 цифр"),
        ("MasterCard Gold abcde1234567890", "Номер карты должен быть строкой из 16 цифр"),
        ("Счет 1234567890123456789", "Номер счета должен быть строкой из 20 цифр"),
        ("Maestro Standard !@#$%^&*()", "Номер карты должен быть строкой из 16 цифр"),
        ("Счет !@#$%^&*()", "Номер счета должен быть строкой из 20 цифр"),
    ]


@pytest.fixture
def valid_dates() -> list:
    # Валидные даты для тестирования преобразования формата
    return [
        ("2024-03-11T02:26:18.671407", "11.03.2024"),
        ("2025-12-31T15:30:00.000000", "31.12.2025"),
        ("2023-01-01T00:00:00.000000", "01.01.2023"),
    ]


@pytest.fixture
def invalid_dates() -> list:
    # Недопустимые даты для проверки ошибок
    return [
        ("2024-03-11", "Недопустимый формат даты"),
        ("2025-12-31T", "Недопустимый формат даты"),
        ("", "Недопустимый формат даты"),
    ]


@pytest.fixture
def sample_transactions() -> list:
    return [
        {
            "id": 939719570,
            "state": "EXECUTED",
            "date": "2018-06-30T02:08:58.425572",
            "operationAmount": {"amount": "9824.07", "currency": {"name": "USD", "code": "USD"}},
            "description": "Перевод организации",
            "from": "Счет 75106830613657916952",
            "to": "Счет 11776614605963066702",
        },
        {
            "id": 142264268,
            "state": "EXECUTED",
            "date": "2019-04-04T23:20:05.206878",
            "operationAmount": {"amount": "79114.93", "currency": {"name": "USD", "code": "USD"}},
            "description": "Перевод со счета на счет",
            "from": "Счет 19708645243227258542",
            "to": "Счет 75651667383060284188",
        },
        {
            "id": 873106923,
            "state": "EXECUTED",
            "date": "2019-03-23T01:09:46.296404",
            "operationAmount": {"amount": "43318.34", "currency": {"name": "руб.", "code": "RUB"}},
            "description": "Перевод со счета на счет",
            "from": "Счет 44812258784861134719",
            "to": "Счет 74489636417521191160",
        },
        {
            "id": 895315941,
            "state": "EXECUTED",
            "date": "2018-08-19T04:27:37.904916",
            "operationAmount": {"amount": "56883.54", "currency": {"name": "USD", "code": "USD"}},
            "description": "Перевод с карты на карту",
            "from": "Visa Classic 6831982476737658",
            "to": "Visa Platinum 8990922113665229",
        },
        {
            "id": 594226727,
            "state": "CANCELED",
            "date": "2018-09-12T21:27:25.241689",
            "operationAmount": {"amount": "67314.70", "currency": {"name": "руб.", "code": "RUB"}},
            "description": "Перевод организации",
            "from": "Visa Platinum 1246377376343588",
            "to": "Счет 14211924144426031657",
        },
    ]
