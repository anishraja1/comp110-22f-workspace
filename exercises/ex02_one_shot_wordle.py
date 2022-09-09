"""One Shot Wordle"""

__author__ = 730575619




secret_word: str = "python" #the secret word the player is trying to guess (can be any number of letters)
length_secret_word = len(secret_word)
response: str = input (f"What is your {length_secret_word} letter guess? ")


WHITE_BOX: str = "\U00002B1C" 
GREEN_BOX: str = "\U0001F7E9"
YELLOW_BOX: str = "\U0001F7E8"
index: int = 0
emoji: str = ""
status: str = "Woo! You got it!"

while len(response) != length_secret_word: #If the user enters a word that is not 6 letters long, they will be continually asked for user input
    response: str = input (f"That was not {length_secret_word} letters! Try again: ")

while index < length_secret_word: #this goes through all the indexes (6) in the user's word
    if response[index] == secret_word[index]: #if the response letter at the index matches the secret word, a green box will be added to the emoji
        emoji += GREEN_BOX
        index += 1
    elif response[index] in secret_word: #if the letter is in the word, a yellow box is added
        emoji += YELLOW_BOX
        index += 1
        status = "Not quite. Play again soon!"
    else:
        emoji += WHITE_BOX #if there is no match, a grey box is added
        index += 1
        python = "Not quite. Play again soon!"



print(emoji) #prints the emoji (6 boxes of either green, yellow, or grey color)
print(status)