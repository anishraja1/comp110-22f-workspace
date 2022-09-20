"""Structured Wordle."""
__author__ = "730575619"


def contains_char(string_word: str, string_character: str) -> bool:  # determines if letter is present in word (says True or False)
    """When given two strings, it will return True if the single character of the second string is found at any index of the first string, and return False if otherwise."""
    assert len(string_character) == 1
    index: int = 0
    while index < len(string_word):
        if string_word[index] == string_character:
            return True  # Either Green or Yellow Box
        else:
            index += 1
    return False  # White Box


def emojified(guess: str, secret: str) -> str:
    """Uses contains_char to add yellow or white boxes depending on if a letter is found in a word. This function then goes further to see if the letter is at the correct index to display a green box."""
    assert len(guess) == len(secret)
    WHITE_BOX: str = "\U00002B1C" 
    GREEN_BOX: str = "\U0001F7E9"
    YELLOW_BOX: str = "\U0001F7E8"
    index: int = 0
    emoji: str = ""

    while index < len(secret):  # Adds appropriate emoji box (further tests for green or yellow)
        if contains_char(secret, guess[index]):
            if guess[index] == secret[index]:
                emoji += GREEN_BOX
                index += 1
            else:
                emoji += YELLOW_BOX
                index += 1
        else:
            emoji += WHITE_BOX
            index += 1
    return emoji  # prints the emoji (6 boxes of either green, yellow, or grey color)


def input_guess(expected_length: int) -> str:  # makes sure user enters a word that is of appropriate length
    """Ensures user input is a correct length."""
    ask: str = input(f"Enter a {expected_length} character word: ")
    while len(ask) != expected_length:
        ask = input(f"That wasn't {expected_length} chars! Try again: ")
    return ask

    
def main() -> None:  # main function; runs the game incorporating multiple functions and stops when the user loses or wins
    """The entrypoint of the program and main game loop."""
    turn: int = 1
    status: int = 0
    while turn <= 6 and status == 0:
        print(f"== Turn {turn}/6 ==")
        guess = input_guess(5)
        print(emojified(guess, "codes"))
        if guess == "codes":
            print(f"You won in {turn}/6 turns!")
            status = 1
        else:
            turn += 1
    if status == 1:
        pass
    else:
        print("X/6 - Sorry, try again tomorrow!")


if __name__ == "__main__":  # makes the game playable as a module
    main()