import pytest
from lib.grammar_checker import *

def test_check_grammar_uppercase_letter():
    assert check_grammar("Test!") == True

def test_check_grammar_lowercase_letter():
    assert check_grammar("test!") == False

def test_check_grammar_period():
    assert check_grammar("Test.") == True

def test_check_grammar_exclamation():
    assert check_grammar("Test!") == True

def test_check_grammar_question_mark():
    assert check_grammar("Test?") == True

def test_check_grammar_no_punctuation():
    assert check_grammar("Test") == False

def test_check_grammar_empty():
    with pytest.raises(Exception) as e:
        check_grammar("")
    assert str(e.value) == "Input is empty."

def test_check_grammar_spaces():
    with pytest.raises(Exception) as e:
        check_grammar("   ")
    assert str(e.value) == "Input is empty."

def test_check_grammar_none():
    with pytest.raises(Exception) as e:
        check_grammar(None)
    assert str(e.value) == "Argument must be string."

def test_check_grammar_number():
    with pytest.raises(Exception) as e:
        check_grammar(1)
    assert str(e.value) == "Argument must be string."

def test_check_grammar_list():
    with pytest.raises(Exception) as e:
        check_grammar(["test"])
    assert str(e.value) == "Argument must be string."