# Reading Time Function Design Recipe

## 1. Describe the Problem

> As a user
> So that I can manage my time
> I want to see an estimate of reading time for a text, assuming that I can read 200 words a minute.

> 200 words = 60 seconds
> 1 word    = 0.3 seconds

## 2. Design the Function Signature

_Include the name of the function, its parameters, return value, and side effects._

```python

def reading_time(text):
    """
    _Extracts reading time for a given text (assuming 200 words a minute)

    Parameters: (list all parameters and their types)
        text: a string containing words e.g. "hello my name is Lauren Miller and I like dogs"

    Returns: (state the return value and its type)
        time in seconds e.g. 10 seconds

    Side effects: (state any side effects)
        This function doesn't print anything or have any other side-effects
    """
    pass
```

## 3. Create Examples as Tests

_Make a list of examples of what the function will take and return._

```python
# EXAMPLE

"""
Given a text with 200 words
It returns a string "60 seconds"
"""
reading_time(Method that joins string of 200 words) => "60.0 seconds"

"""
Given a text with 10 words
It returns a string "3.0 seconds"
"""
reading_time("Hello my name is Lauren Miller and I like dogs") => "3 seconds"

"""
Given an empty text
It returns an error
"""
reading_time("") => "Can't estimate a reading time for an empty text"
```

## 4. Implement the Behaviour

_After each test you write, follow the test-driving process of red, green, refactor to implement the behaviour._

```python

from lib.reading_time import *

"""
Given a text with 10 words
It returns an integer of 3 (how many seconds it takes to read the text)
"""
def test_reading_time_10_words():
    result = reading_time("Hello my name is Lauren Miller and I like dogs")
    assert result == "3 seconds"
```