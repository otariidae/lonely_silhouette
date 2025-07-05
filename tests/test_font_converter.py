from lonely_silhouette.font_converter import FontConverter, FontStyle


def test_italicizer() -> None:
    italicizer = FontConverter.create(FontStyle.ITALIC)
    assert italicizer is not None
    actual = italicizer.convert("silhouette")
    assert actual == "𝑠𝑖𝑙ℎ𝑜𝑢𝑒𝑡𝑡𝑒"


def test_scriptizer() -> None:
    scriptizer = FontConverter.create(FontStyle.SCRIPT)
    assert scriptizer is not None
    actual = scriptizer.convert("silhouette")
    assert actual == "𝓈𝒾𝓁𝒽ℴ𝓊ℯ𝓉𝓉ℯ"
