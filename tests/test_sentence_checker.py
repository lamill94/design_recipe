from lib.sentence_checker import *

# Given a text that starts with capital letter & ends in full-stop
# Return True

def test_sentence_checker_text_has_capital_letter_and_full_stop():
    result = sentence_checker("Hello my name is Lauren.")
    assert result == True

# Given a text that starts with capital letter & ends in exclamation mark
# Return True

def test_sentence_checker_text_has_capital_letter_and_exclamation_mark():
    result = sentence_checker("Hello my name is Lauren!")
    assert result == True

# Given a text that starts with capital letter & ends in question mark
# Return True

def test_sentence_checker_text_has_capital_letter_and_question_mark():
    result = sentence_checker("Hello my name is Lauren?")
    assert result == True

# Given a text that starts with capital letter & doesn't end in "suitable sentence-ending punctuation mark"
# Return False

def test_sentence_checker_text_has_capital_letter_and_no_punctuation_at_end():
    result = sentence_checker("Hello my name is Lauren")
    assert result == False

# Given a text that doesn't start with capital letter & ends in full-stop
# Return False

def test_sentence_checker_text_has_no_capital_letter_and_full_stop():
    result = sentence_checker("hello my name is Lauren.")
    assert result == False

# Given a text that doesn't start with capital letter & ends in exclamation mark
# Return False

def test_sentence_checker_text_has_no_capital_letter_and_exclamation_mark():
    result = sentence_checker("hello my name is Lauren!")
    assert result == False

# Given a text that doesn't start with capital letter & ends in question mark
# Return False

def test_sentence_checker_text_has_no_capital_letter_and_question_mark():
    result = sentence_checker("hello my name is Lauren?")
    assert result == False

# Given a text that doesn't start with capital letter & doesn't end in "suitable sentence-ending punctuation mark"
# Return False

def test_sentence_checker_text_has_no_capital_letter_and_no_punctuation_at_end():
    result = sentence_checker("hello my name is Lauren")
    assert result == False

# Given an empty text
# Return error

def test_sentence_checker_empty_text():
    with pytest.raises(Exception) as e:
        sentence_checker("")
        error_message = str(e.value)
        assert error_message == "Error - please enter text to check"
    