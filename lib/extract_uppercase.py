import re

def extract_uppercase(text):
    words = re.split(r"\W+", text)
    upper_case_words = [word for word in words if word.isupper()]
    return upper_case_words