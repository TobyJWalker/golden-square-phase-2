from lib.count_words import *

'''
A function called count_words that takes a string as an argument
Returns the amount of words in the string
'''
def test_count_words_one_word():
    assert count_words("test") == 1

def test_count_words_two_words():
    assert count_words("test test") == 2

def test_count_words_empty():
    assert count_words("") == 0