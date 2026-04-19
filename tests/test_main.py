from io import StringIO
import pytest
from lonely_silhouette.__main__ import main

with open("tests/test_jmdict.xml", "rb") as f:
    MOCKED_JMDICT_CONTENT = f.read()


def test_main_with_args(capsys, respx_mock):
    respx_mock.get("http://ftp.edrdg.org/pub/Nihongo/JMdict_e").respond(
        200, content=MOCKED_JMDICT_CONTENT
    )
    main(["いや待て、この孤独なシルエットは…？"])
    captured = capsys.readouterr()
    assert captured.out.strip() == "いや待て、この孤独な𝑠𝑖𝑙ℎ𝑜𝑢𝑒𝑡𝑡𝑒は…？"


def test_main_with_stdin(capsys, monkeypatch, respx_mock):
    monkeypatch.setattr("sys.stdin", StringIO("いや待て、この孤独なシルエットは…？\n"))
    respx_mock.get("http://ftp.edrdg.org/pub/Nihongo/JMdict_e").respond(
        200, content=MOCKED_JMDICT_CONTENT
    )
    main([])
    captured = capsys.readouterr()
    assert captured.out.strip() == "いや待て、この孤独な𝑠𝑖𝑙ℎ𝑜𝑢𝑒𝑡𝑡𝑒は…？"


def test_main_with_font_style(capsys, respx_mock):
    respx_mock.get("http://ftp.edrdg.org/pub/Nihongo/JMdict_e").respond(
        200, content=MOCKED_JMDICT_CONTENT
    )
    main(["--font-style", "script", "いや待て、この孤独なシルエットは…？"])
    captured = capsys.readouterr()
    assert captured.out.strip() == "いや待て、この孤独な𝓈𝒾𝓁𝒽ℴ𝓊ℯ𝓉𝓉ℯは…？"


def test_main_with_help(respx_mock):
    with pytest.raises(SystemExit) as e:
        respx_mock.get("http://ftp.edrdg.org/pub/Nihongo/JMdict_e").respond(
            200, content=MOCKED_JMDICT_CONTENT
        )
        main(["--help"])
    assert e.value.code == 0


def test_main_without_args(monkeypatch, respx_mock):
    with pytest.raises(SystemExit) as e:
        monkeypatch.setattr("sys.stdin.isatty", lambda: True)
        respx_mock.get("http://ftp.edrdg.org/pub/Nihongo/JMdict_e").respond(
            200, content=MOCKED_JMDICT_CONTENT
        )
        main([])
    assert e.value.code == 1
