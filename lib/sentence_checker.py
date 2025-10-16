import pytest

def sentence_checker(text):

    punctuation = ['.', '!', '?']

    if text == "":
        raise Exception("Error - please enter text to check")
    else:
        return text[0].isupper() and text[-1] in punctuation
