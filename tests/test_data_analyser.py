import pytest
from analyser.data_analyser import DataAnalyser

@pytest.fixture
def sample_data() -> list:
    return [
        "Hello world!\n",
        "\tThis is a test. ",
        "Another line with words.  ",
        "Words words words."
    ]


@pytest.fixture
def analyser(sample_data) -> DataAnalyser:
    return DataAnalyser(sample_data)


def test_clean_data(sample_data):
    cleaned: list = DataAnalyser._clean_data(sample_data)
    expected: list = [
        "Hello world!",
        "This is a test.",
        "Another line with words.",
        "Words words words."
    ]
    assert cleaned == expected


def test_amount_of_lines(analyser):
    assert analyser.amount_of_lines() == 4


def test_amount_of_words(analyser):
    # "Hello world!" = 2, "This is a test." = 4, "Another line with words." = 4, "Words words words." = 3
    assert analyser.amount_of_words() == 13


def test_amount_of_letters(analyser):
    # Remove spaces:
    # "Helloworld!" = 11, "Thisisatest." = 12, "Anotherlinewithwords." = 21, "Wordswordswords." = 16
    total_letters : int = 11 + 12 + 21 + 16
    assert analyser.amount_of_letters() == total_letters


def test_five_most_frequent_words(analyser):
    expected: list = [
        ('words.', 2),
        ('Hello', 1),
        ('world!', 1),
        ('This', 1),
        ('is', 1)
    ]
    result: list = analyser.show_five_most_frequent_words()
    assert result[:5] == expected


def test_empty_input():
    empty_analyser: DataAnalyser = DataAnalyser([])
    assert empty_analyser.amount_of_lines() == 0
    assert empty_analyser.amount_of_words() == 0
    assert empty_analyser.amount_of_letters() == 0
    assert empty_analyser.show_five_most_frequent_words() == []


def test_tied_frequencies():
    data: list = ["apple banana", "apple orange", "banana orange"]
    analyser: DataAnalyser = DataAnalyser(data)
    result: list = analyser.show_five_most_frequent_words()
    expected_words: dict = {'apple': 2, 'banana': 2, 'orange': 2}
    result_dict = dict(result)
    assert all(word in expected_words for word in result_dict)
    assert all(result_dict[word] == expected_words[word] for word in result_dict)
