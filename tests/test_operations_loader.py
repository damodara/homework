from unittest.mock import MagicMock, patch

import pytest

from src.operations_loader import read_csv, read_operations, read_xlsx


def test_read_csv() -> None:
    path = "/tmp/data.csv"
    expected = [{"id": 1, "amount": 100.0}, {"id": 2, "amount": 200.0}]

    with patch("src.operations_loader.pd.read_csv") as mock_read:
        df = MagicMock()
        df.to_dict.return_value = expected
        mock_read.return_value = df

        result = read_csv(path)

        mock_read.assert_called_once_with(path)
        df.to_dict.assert_called_once_with(orient="records")
        assert result == expected


def test_read_xlsx() -> None:
    path = "/tmp/data.xlsx"
    expected = [{"id": 1, "amount": 100.0}, {"id": 2, "amount": 200.0}]

    with patch("src.operations_loader.pd.read_excel") as mock_read:
        df = MagicMock()
        df.to_dict.return_value = expected
        mock_read.return_value = df

        result = read_xlsx(path)

        mock_read.assert_called_once_with(path)
        df.to_dict.assert_called_once_with(orient="records")
        assert result == expected


def test_read_csv_raises_runtime_on_generic_error() -> None:
    with patch("src.operations_loader.pd.read_csv", side_effect=Exception("boom")):
        with pytest.raises(RuntimeError) as exc:
            read_csv("/tmp/x.csv")
        assert "Ошибка чтения CSV" in str(exc.value)


def test_read_xlsx_raises_runtime_on_generic_error() -> None:
    with patch("src.operations_loader.pd.read_excel", side_effect=Exception("boom")):
        with pytest.raises(RuntimeError) as exc:
            read_xlsx("/tmp/x.xlsx")
        assert "Ошибка чтения XLS/XLSX" in str(exc.value)


def test_read_operations_dispatches_to_csv() -> None:
    path = "/tmp/file.csv"
    with patch("src.operations_loader.os.path.splitext", return_value=("/tmp/file", ".csv")):
        with patch("src.operations_loader.read_csv", return_value=[{"ok": 1}]) as mock_csv:
            result = read_operations(path)
            mock_csv.assert_called_once_with(path)
            assert result == [{"ok": 1}]


def test_read_operations_dispatches_to_xlsx() -> None:
    path = "/tmp/file.xlsx"
    with patch("src.operations_loader.os.path.splitext", return_value=("/tmp/file", ".xlsx")):
        with patch("src.operations_loader.read_xlsx", return_value=[{"ok": 2}]) as mock_xlsx:
            result = read_operations(path)
            mock_xlsx.assert_called_once_with(path)
            assert result == [{"ok": 2}]


def test_read_operations_raises_on_unsupported_extension() -> None:
    with patch("src.operations_loader.os.path.splitext", return_value=("/tmp/file", ".txt")):
        with pytest.raises(ValueError):
            read_operations("/tmp/file.txt")
