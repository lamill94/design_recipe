# Sentence Checker Function Design Recipe

## 1. Describe the Problem

_Put or write the user story here. Add any clarifying notes you might have._

> As a user
> So that I can improve my grammar
> I want to verify that a text starts with a capital letter and ends with a suitable sentence-ending punctuation mark.

> Note: suitable sentence-ending punctuation mark - . ! ?

## 2. Design the Function Signature

_Include the name of the function, its parameters, return value, and side effects._

```python

def sentence_checker(text):
    """
    Params:
        text: a string e.g. Hello my name is Lauren.

    Returns:
        True: if text starts with capital letter & "suitable sentence-ending punctuation mark" e.g. . ! ?
        False: if above conditions aren't met

    Side effects:
        None
    """
```

## 3. Create Examples as Tests

_Make a list of examples of what the function will take and return._

```python

# BOTH CONDITIONS TRUE

"""
Given a text that starts with capital letter & ends in full-stop
Return True
"""
sentence_checker("Hello my name is Lauren.") => True

"""
Given a text that starts with capital letter & ends in exclamation mark
Return True
"""
sentence_checker("Hello my name is Lauren!") => True

"""
Given a text that starts with capital letter & ends in question mark
Return True
"""
sentence_checker("Hello my name is Lauren?") => True

# ONE CONDITION TRUE, ONE CONDITION FALSE

"""
Given a text that starts with capital letter & doesn't end in "suitable sentence-ending punctuation mark"
Return False
"""
sentence_checker("Hello my name is Lauren") => False

"""
Given a text that doesn't start with capital letter & ends in full-stop
Return False
"""
sentence_checker("hello my name is Lauren.") => False

"""
Given a text that doesn't start with capital letter & ends in exclamation mark
Return False
"""
sentence_checker("hello my name is Lauren!") => False

"""
Given a text that doesn't start with capital letter & ends in question mark
Return False
"""
sentence_checker("hello my name is Lauren?") => False

# BOTH CONDITIONS FALSE

"""
Given a text that doesn't starts with capital letter & doesn't end in "suitable sentence-ending punctuation mark"
Return False
"""
sentence_checker("hello my name is Lauren") => False

# ERROR

"""
Given an empty text
Return error
"""
sentence_chcker("") => "Error - please enter text to check"

```

## 4. Implement the Behaviour

_After each test you write, follow the test-driving process of red, green, refactor to implement the behaviour._

```python

from lib.sentence_checker import *

"""
Given a text that starts with capital letter & ends in full-stop
Return True
"""

def test_sentence_checker_text_has_capital_letter_and_full_stop():
    result = sentence_checker("Hello my name is Lauren.")
    assert result == True

```
