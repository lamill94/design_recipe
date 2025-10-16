from lib.reading_time import *
import pytest

# Given a text with 200 words
# It returns a string of "60.0 seconds"

def test_reading_time_200_words():
    text = " ".join(["word" for i in range(0, 200)])
    result = reading_time(text)
    assert result == "60.0 seconds"

# Given a text with 10 words
# It returns a string of "3.0 seconds"

def test_reading_time_10_words():
    result = reading_time("Hello my name is Lauren Miller and I like dogs")
    assert result == "3.0 seconds"

# Given an empty text
# It returns an error

def test_reading_time_empty_text():
    with pytest.raises(Exception) as e:
        reading_time("")
        error_message = str(e.value)
        assert error_message == "Can't estimate a reading time for an empty text"