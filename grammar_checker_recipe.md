# {{PROBLEM}} Function Design Recipe

## 1. Describe the Problem

As a user
So that I can improve my grammar
I want to verify that a text starts with a capital letter and ends with a suitable sentence-ending punctuation mark.

## 2. Design the Function Signature

```python

def estimate_reading_time(mixed_words):
    """Checks if a text starts with a capital letter and ends with a suitable sentence-ending punctuation mark.

    Parameters: (list all parameters and their types)
        text: A string

    Returns: (state the return value and its type)
        A boolean value stating if its valid or not

    Side effects: (state any side effects)
        Error if non string value
        Error if empty string
    """
    pass # Test-driving means _not_ writing any code here yet.
```

## 3. Create Examples as Tests

_Make a list of examples of what the function will take and return._

```python

"""
Given a string
Check if the first character is an uppercase letter
"""
check_grammar("Hello") => True

"""
Given a string
Check if the last character is a punctuation mark
"""
check_grammar("Hello.") => True
check_grammar("Hello!") => True
check_grammar("Hello?") => True
check_grammar("Hello") => False

"""
Given a string
Raise an error if it is an empty string
"""
check_grammar("") raises Error
check_grammar(" ") raises Error

"""
Given a non-string value
Raise an error
"""
check_grammar(1) raises Error
check_grammar([]) raises Error
check_grammar(None) raises Error


```

## 4. Implement the Behaviour

_After each test you write, follow the test-driving process of red, green, refactor to implement the behaviour._
