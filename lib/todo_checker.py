def check_for_todo(text):
    if type(text) != str:
        raise TypeError("Input must be a string")
    elif text =="":
        raise Exception("Input must not be empty")
    return "#TODO" in text