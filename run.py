import random
from words import word_list


print("Welcome to Hangman, let's play!")

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

def print_hangman(wrong):
  if(wrong == 0):
    print("\n+---+")
    print("    |")
    print("    |")
    print("    |")
    print("   ===")
  elif(wrong == 1): 
    print("\n+---+")
    print("O   |")
    print("    |")
    print("    |")
    print("   ===")
  elif(wrong == 2):
    print("\n+---+")
    print("O   |")
    print("|   |")
    print("    |")
    print("   ===")
  elif(wrong == 3):
    print("\n+---+")
    print(" O  |")
    print("/|  |")
    print("    |")
    print("   ===")
  elif(wrong == 4):
    print("\n+---+")
    print(" O  |")
    print("/|\ |")
    print("    |")
    print("   ===")
  elif(wrong == 5):
    print("\n+---+")
    print(" O  |")
    print("/|\ |")
    print("/   |")
    print("   ===")
  elif(wrong == 6):
    print("\n+---+")
    print(" O   |")
    print("/|\  |")
    print("/ \  |")
    print("    ===")