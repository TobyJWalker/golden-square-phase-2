# {{PROBLEM}} Function Design Recipe

## 1. Describe the Problem

>> As a user
>> So that I can keep track of my tasks
>> I want to check if a text includes the string #TODO.

## 2. Design the Function Signature

```python

def check_for_todo(text):
    """
    Purpose: Check if #TODO is in the text

    Parameters: (list all parameters and their types)
        text: a string

    Returns: (state the return value and its type)
        boolean representing if todo is in the text

    Side effects: (state any side effects)
        Raise an error if text is not a string
        Raise an error if string is empty
    """
    pass # Test-driving means _not_ writing any code here yet.
```

## 3. Create Examples as Tests

_Make a list of examples of what the function will take and return._

```python

"""
Given a non-string value
raise an error
"""
check_for_todo(1) raises error
check_for_todo([]) raises error
check_for_todo(None) raises error

"""
Given a string
raise error if string is empty
"""
check_for_todo("") raises error

"""
Given a string
check if #TODO is in the text
"""
check_for_todo("#TODO do the dishes") => True
check_for_todo("do the dishes") => False

```

## 4. Implement the Behaviour

_After each test you write, follow the test-driving process of red, green, refactor to implement the behaviour._
