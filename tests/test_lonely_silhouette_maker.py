from pathlib import Path
from lonely_silhouette.lonely_silhouette_maker import LonelySilhouetteMaker
from lonely_silhouette.font_converter import FontConverter, FontStyle


def test_make() -> None:
    jmdict_e_xml_path = Path("tests/test_jmdict.xml")
    maker = LonelySilhouetteMaker(jmdict_e_xml_path)
    font_converter = FontConverter.create(FontStyle.ITALIC)
    text = "いや待て、この孤独なシルエットは…？"
    actual = maker.make(text, font_converter)
    assert actual == "いや待て、この孤独な𝑠𝑖𝑙ℎ𝑜𝑢𝑒𝑡𝑡𝑒は…？"
