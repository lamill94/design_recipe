def reading_time(text):
    if text == "":
        raise Exception("Can't estimate a reading time for an empty text")
    else:
        word_count = len(text.split())
        time_in_seconds = word_count * 0.3
        return str(time_in_seconds) + " seconds"