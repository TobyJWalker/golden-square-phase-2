from lib.exercise_1 import *

def test_make_snippet_one_word():
    assert make_snippet("test") == "test"

def test_make_snippet_two_words():
    assert make_snippet("test test") == "test test"

def test_make_snippet_five_words():
    assert make_snippet("test test test test test") == "test test test test test"

def test_make_snippet_six_words():
    assert make_snippet("test test test test test test") == "test test test test test ..."