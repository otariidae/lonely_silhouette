import pytest
from lonely_silhouette.part_of_speech import PartOfSpeech


@pytest.mark.parametrize(
    "raw_part_of_speech, expected_category, expected_subcategory1, expected_subcategory2, expected_subcategory3",
    [
        ("名詞,一般,*,*", "名詞", "一般", "*", "*"),
        ("名詞,固有名詞,地域,一般", "名詞", "固有名詞", "地域", "一般"),
        ("動詞,自立,*,*", "動詞", "自立", "*", "*"),
    ],
)
def test_from_raw_part_of_speech(
    raw_part_of_speech,
    expected_category,
    expected_subcategory1,
    expected_subcategory2,
    expected_subcategory3,
):
    part_of_speech = PartOfSpeech.from_raw_part_of_speech(raw_part_of_speech)
    assert part_of_speech.category == expected_category
    assert part_of_speech.subcategory1 == expected_subcategory1
    assert part_of_speech.subcategory2 == expected_subcategory2
    assert part_of_speech.subcategory3 == expected_subcategory3
