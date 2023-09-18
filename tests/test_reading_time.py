import pytest
from lib.reading_time import *

with open("100_word_text.txt", "r") as f:
    hundred_word_text = f.read()

with open("200_word_text.txt", "r") as f:
    two_hundred_word_text = f.read()

def test_reading_time_two_hundred_words():
    assert estimate_reading_time(two_hundred_word_text) == 1

def test_reading_time_hundred_words():
    assert estimate_reading_time(hundred_word_text) == 0.5

def test_reading_time_empty():
    assert estimate_reading_time("") == 0

def test_reading_time_spaces():
    assert estimate_reading_time("   ") == 0

def test_reading_time_number():
    with pytest.raises(TypeError) as e:
        estimate_reading_time(1)
    return str(e.value) == "Argument must be a string"

def test_reading_time_none():
    with pytest.raises(TypeError) as e:
        estimate_reading_time(None)
    return str(e.value) == "Argument must be a string"

def test_reading_time_list():
    with pytest.raises(TypeError) as e:
        estimate_reading_time(['this', 'is', 'a', 'list'])
    return str(e.value) == "Argument must be a string"