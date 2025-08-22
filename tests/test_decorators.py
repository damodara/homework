import pytest

from src.decorators import log


@pytest.fixture
def capsys(request) -> pytest.CaptureFixture[str]:
    return request.getfixturevalue("capsys")


def test_log_success(capsys: pytest.CaptureFixture[str]) -> None:
    @log()
    def add(a, b):
        return a + b

    add(2, 3)
    captured = capsys.readouterr()
    assert "add completed successfully with result: 5" in captured.out
