


def Love(subject: str) -> str:
    """Given a subject as a parameter, returns a loving string"""
    return f"I love you {subject} !"


def spread_love(to: str, n:int) -> str:
    """Generate a string repeating a loving message n times"""
    love_note: str = ""
    i: int = 0
    while i < n:
        love_note += Love(to)+ "\n"
        i += 1
    return love_note


print(spread_love("hello",3))


