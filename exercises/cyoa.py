"""Choose your own adventure!"""


from random import randint  # Randint allows for a random number to be generated from a specified range.


SOUL_POINTS_GAIN: int = 4  # Number of points gained from a victory
SOUL_POINTS_LOSS: int = 1  # Number of points lost from a loss
LOSS_DEMON: str = "\U0001F608"  # Devil Smiling Emoji; loss in fighting 
LOSS_SAD: str = "\U0001F613"  # Sad Emoji; loss in bonus game	
WIN_MEDAL: str = "\U0001F3C5"  # Medal Emoji
soul_points: int = 0  # Global Variable
player: str = ""  # Global Variable


def greet() -> str:
  """Gives context about the game and greets the player."""
  global player
  print("In this game, you will battle demons and collect their souls! To kill a demon, you must try to guess a randomly generated number from 1-3. If you guess correctly, you will kill the demon and collect 5 soul points. If you guess incorrectly, you will lose 2 soul points and the demon will get away. In between rounds, you can choose to earn/lose bonus points. You will have to guess heads or tails. If your guess matches the coin flip result, your soul points double. If not, they are halved.\n")
  player = input("What is your name fellow adventurer? ")
  print(f"Hello {player}, good luck on your journey!\n")


def end_game() -> None:
  """Game ends and displays the player's score."""
  print(f"\n\nThanks for playing!\nYou have accumulated {soul_points} soul points!")  # Goodbye Message
  quit()  # quits the entire game


def fight(soul_point_value) -> int:
  """Player continues on their journey to kill demons and earn points."""
  secret_number: int = randint(1,3)  # Number player has to guess to gain soul points.
  guess: str = input("Guess a number from 1-3. If you're correct, you'll deal damage! ")
  if int(guess) == secret_number:  # If they guess correctly, they get soul points. If not, they lsoe soul points.
    return 0  # Change occurs in main function
  else:
    return 1  # Change occurs in main function


def bonus() -> None:
  """Chance to double or halve the player's points."""
  global soul_points
  deciphered_value: int = 2  # 2 means that the while loop hasn't gotten a valid response yet. 0 and 1 means it has.
  secret_number: int = randint(0,1)
  while deciphered_value == 2:
    guess: str = input(f"Hello {player}, feeling lucky? Guess heads(h) or tails(t): ")
    if guess == "h":
      deciphered_value = 0
    elif guess == "t":
      deciphered_value = 1
    else:
      pass
  if deciphered_value == secret_number:  # Directly changes the soul_points global variable
    print(WIN_MEDAL)
    soul_points = soul_points * 2
  else:
    print(LOSS_SAD)
    soul_points = soul_points // 2


def main() -> None:
  while True:
    """The main function that runs the game and number generating algoritm."""
    global soul_points
    player_response: str = input("Do you want to fight(f), quit(q), or potentially win some bonus points(b)? ")
    if player_response == "q":  # quits game
      end_game()
    elif player_response == "b":  # chance to earn bonus points or lose some...
      bonus()
    elif player_response == "f":  # fight to gain or lose soul points
      if fight(soul_points) == 0:
        print(WIN_MEDAL)
        soul_points += SOUL_POINTS_GAIN  # direct change to the globals variable
      else:
        print(LOSS_DEMON)
        soul_points -= SOUL_POINTS_LOSS  # direct change to the globals variable
    else:
      print("Sorry, that was not a valid response. Please try again.")  # If user doesn't enter f, q, or b, then they will be prompted to this message.
    print(f"Soul Points: {soul_points}")  # Displays the player's soul points at the end of each round.


if __name__ == "__main__":  # Playable module
  greet()  # Greets Player
  main()  # Main Function