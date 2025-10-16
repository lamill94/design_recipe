from lib.extract_uppercase import *

# Given a lower and an uppercase word
# It returns a list with the uppercase word

def test_extract_uppercase_with_lower_and_upper():
    result = extract_uppercase("hello WORLD")
    assert result == ["WORLD"]

# Given two uppercase words
# It returns a list with both words

def test_extract_uppercase_with_two_upper():
    result = extract_uppercase("HELLO WORLD")
    assert result == ["HELLO", "WORLD"]

# Given two lowercase words
# It returns an empty list

def test_extract_uppercase_with_two_lower():
    result = extract_uppercase("hello world")
    assert result == []

# Given a lower and a mixed case word
# It returns an empty list

def test_extract_uppercase_with_lower_and_mixed():
    result = extract_uppercase("hello WoRLD")
    assert result == []

# Given a lowercase word and an uppercase word with an exclamation mark
# It returns a list with the uppercase word, no exclamation mark

def test_extract_uppercase_with_lower_and_upper_with_exclamation():
    result = extract_uppercase("hello WORLD!")
    assert result == ["WORLD"]

# Given an empty string
# It returns an empty list

def test_extract_uppercase_with_empty_string():
    result = extract_uppercase("")
    assert result == []

# Given a None value
# It throws an error

# extract_uppercase(None) throws an error