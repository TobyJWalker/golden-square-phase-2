import pytest
from lib.todo_checker import *

def test_todo_checker_number():
    with pytest.raises(TypeError) as e:
        check_for_todo(1)
    assert str(e.value) == "Input must be a string"

def test_todo_checker_list():
    with pytest.raises(TypeError) as e:
        check_for_todo(["test"])
    assert str(e.value) == "Input must be a string"

def test_todo_checker_none():
    with pytest.raises(TypeError) as e:
        check_for_todo(None)
    assert str(e.value) == "Input must be a string"

def test_todo_checker_empty():
    with pytest.raises(Exception) as e:
        check_for_todo("")
    assert str(e.value) == "Input must not be empty"

def test_todo_checker_no_todo():
    assert check_for_todo("do the dishes") == False

def test_todo_checker_todo():
    assert check_for_todo("#TODO do the dishes") == True