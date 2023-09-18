def estimate_reading_time(text):

    if type(text) != str:
        raise TypeError("Argument must be a string")
    
    reading_speed = 200 # words per minute
    word_list = text.split()
    return len(word_list) / reading_speed