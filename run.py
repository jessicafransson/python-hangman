import random
"""from words import word_list"""

print("Welcome to Hangman, let's play!")
print("________________________________")

wordDictionary = ["appartment", "house", "flowers", "diamonds", "python", "javascript", "singer", "music", "developer"]

""" 
Choose a random word
"""
randomWord = random.choice(wordDictionary)

for x in randomWord:
  print("_", end="")

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

def print_hangman(wrong):
  """
  Get the symbol of hangman displayed when wrong guesses are made
  """
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

def printWord(guessedLetters):
  """ Display the guesses being made and counter
  """
  counter=0
  rightLetters=0
  for char in randomWord:
    if(char in guessedLetters):
      print(randomWord[counter], end=" ")
      rightLetters+=1
    else:
      print(" ", end=" ")
    counter+=1
  return rightLetters