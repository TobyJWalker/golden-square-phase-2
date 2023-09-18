def make_snippet(text):
    words = text.split()
    return " ".join(words[:5]) + (" ..." if len(words) > 5 else "")