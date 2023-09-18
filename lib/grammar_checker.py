def check_grammar(text):
    if type(text) != str:
        raise Exception("Argument must be string.")
    elif text == "" or text.isspace():
        raise Exception("Input is empty.")
    return text[0].isupper() and any(c == text[-1] for c in [".", "!", "?"])