import random
from words import word_list


print("Welcome to Hangman, let's play!")
    """
    Welcome message for the players to know what game this is
    """

def get_word():
  """ 
  Get the words to uppercase for easier readability
  """
  word = random.choice(word_list)
  return word.upper()

def get_random_word():
  """
  Pick a random word from text file to be used in the game
  """
  random_word = random.choice(open("words.py", "r").read().split('\n'))
  return random_word.upper()

def initialise_game():
  """
  Options for player to select play game, or see game rules
  """
  print(" Press " + "1" + "to play game")
  print(" Press " + "2" + "to view rules")
  options = False
  while not options:
    settings = input("\n")
    if settings == "1":
      options = True
      difficulty = "default"
      return difficulty

    elif settings == "2":
      options = True
      game_rules()

    else:
      print("Please select 1 or 2", "choice")




HANGMANPICS = ['''
  +---+
  |   |
      |
      |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
      |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
  |   |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|   |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|\  |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|\  |
 /    |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|\  |
 / \  |
      |
=========
]