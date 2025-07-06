# mypy: disable-error-code=no-untyped-def
from io import StringIO
from unittest.mock import patch, Mock
import pytest
from lonely_silhouette.__main__ import main

with open("tests/test_jmdict.xml", "rb") as f:
    MOCKED_JMDICT_CONTENT = f.read()


def mock_requests_get(url, *args, **kwargs):
    """requests.get のモック。指定されたJMDictのURLに対してのみ test_jmdict.xml の内容を返す。"""
    if url == "http://ftp.edrdg.org/pub/Nihongo/JMdict_e":
        mock_response = Mock()
        mock_response.content = MOCKED_JMDICT_CONTENT
        mock_response.raise_for_status.return_value = None
        return mock_response
    else:
        raise RuntimeError(f"Network access to {url} is forbidden during tests!")


def test_main_with_args(capsys) -> None:
    with patch("requests.get", side_effect=mock_requests_get):
        main(["いや待て、この孤独なシルエットは…？"])
        captured = capsys.readouterr()
        assert captured.out.strip() == "いや待て、この孤独な𝑠𝑖𝑙ℎ𝑜𝑢𝑒𝑡𝑡𝑒は…？"


def test_main_with_stdin(capsys, monkeypatch) -> None:
    monkeypatch.setattr("sys.stdin", StringIO("いや待て、この孤独なシルエットは…？\n"))
    with patch("requests.get", side_effect=mock_requests_get):
        main([])
        captured = capsys.readouterr()
        assert captured.out.strip() == "いや待て、この孤独な𝑠𝑖𝑙ℎ𝑜𝑢𝑒𝑡𝑡𝑒は…？"


def test_main_with_font_style(capsys) -> None:
    with patch("requests.get", side_effect=mock_requests_get):
        main(["--font-style", "script", "いや待て、この孤独なシルエットは…？"])
        captured = capsys.readouterr()
        assert captured.out.strip() == "いや待て、この孤独な𝓈𝒾𝓁𝒽ℴ𝓊ℯ𝓉𝓉ℯは…？"


def test_main_with_help() -> None:
    with pytest.raises(SystemExit) as e:
        with patch("requests.get", side_effect=mock_requests_get):
            main(["--help"])
    assert e.value.code == 0


def test_main_without_args(monkeypatch) -> None:
    with pytest.raises(SystemExit) as e:
        monkeypatch.setattr("sys.stdin.isatty", lambda: True)
        with patch("requests.get", side_effect=mock_requests_get):
            main([])
    assert e.value.code == 1