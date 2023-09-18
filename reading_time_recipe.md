# {{PROBLEM}} Function Design Recipe

## 1. Describe the Problem

>> As a user
>> So that I can manage my time
>> I want to see an estimate of reading time for a text, assuming that I can read 200 words a minute.

## 2. Design the Function Signature

```python

def estimate_reading_time(mixed_words):
    """Estimates the reading time for a provided text assuming a reading speed of 200wpm

    Parameters: (list all parameters and their types)
        text: A string which the program will calculate the reading time of

    Returns: (state the return value and its type)
        a float representing the minutes it takes to read

    Side effects: (state any side effects)
        This function doesn't print anything or have any other side-effects
    """
    pass # Test-driving means _not_ writing any code here yet.
```

## 3. Create Examples as Tests

_Make a list of examples of what the function will take and return._

```python

"""
Given a text with 200 words
return 1
"""
estimate_reading_time({200_word_text}) => 1

"""
Given a text with 100 words
return 0.5 
"""
estimate_reading_time({100_word_text}) => 0.5

"""
Given a text with 0 words
return 0
"""
estimate_reading_time("") => 0

"""
Given a text with spaces
return 0
"""
estimate_reading_time("   ") => 0

"""
"""
Given a non-string value
return an error
"""
estimate_reading_time(1) throws error
estimate_reading_time(None) throws error
estimate_reading_time(['this', 'is', 'a', 'list']) throws error

```

## 4. Implement the Behaviour

_After each test you write, follow the test-driving process of red, green, refactor to implement the behaviour._
