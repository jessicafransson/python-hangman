import random
"""from words import word_list"""

wordDictionary = ["appartment", "house", "flowers", "diamonds", "python", "javascript", "singer", "music",
                  "developer", "system", "book", "movie", "renovation", "display", "credit", "collection", "podcast"]

""" 
Choose a random word
"""
# randomWord = random.choice(wordDictionary)


# def get_random_word():
#   """
#   Pick a random word from text file to be used in the game
#   """
#   random_word = random.choice(open("words.py", "r").read().split('\n'))
#   return random_word.upper()

def print_hangman(wrong):
    """
    Get the symbol of hangman displayed when wrong guesses are made
    """
    if (wrong == 0):
        print("\n+---+")
        print("    |")
        print("    |")
        print("    |")
        print("   ===")
    elif (wrong == 1):
        print("\n+---+")
        print("O   |")
        print("    |")
        print("    |")
        print("   ===")
    elif (wrong == 2):
        print("\n+---+")
        print("O   |")
        print("|   |")
        print("    |")
        print("   ===")
    elif (wrong == 3):
        print("\n+---+")
        print(" O  |")
        print("/|  |")
        print("    |")
        print("   ===")
    elif (wrong == 4):
        print("\n+---+")
        print(" O  |")
        print("/|\ |")
        print("    |")
        print("   ===")
    elif (wrong == 5):
        print("\n+---+")
        print(" O  |")
        print("/|\ |")
        print("/   |")
        print("   ===")
    elif (wrong == 6):
        print("\n+---+")
        print(" O   |")
        print("/|\  |")
        print("/ \  |")
        print("    ===")


def printWord(guessedLetters):
    """ Display the guesses being made and counting
    """
    counter = 0
    rightLetters = 0
    for char in randomWord:
        if (char in guessedLetters):
            print(randomWord[counter].upper(), end=" ")
            rightLetters += 1
        else:
            print(" ", end=" ")
        counter += 1
    return rightLetters


def printLines():
    """
    """
    print("\r")
    for char in randomWord:
        print("\u203E", end=" ")


def check_word_guess(guess, word):
    if guess in word:
        return True
    return False


if __name__ == "__main__":
    randomWord = random.choice(wordDictionary)
    print("Welcome to Hangman, let's play!")
    print("________________________________")
    print_hangman(0)
    for x in randomWord:
        print("_ ", end="")
    lenght_of_word_to_guess = len(randomWord)
    amount_of_times_wrong = 0
    current_guess_index = 0
    current_letters_guessed = []
    current_letters_right = 0

    while (amount_of_times_wrong != 6 and current_letters_right != lenght_of_word_to_guess):
        # print("This is what you have guessed: \n")
        # for letter in current_letters_guessed:
        #   print(letter, end=" ")
        """
        prompt user for input
        """
        letterGuessed = input("\nGuess a letter: ")
        """
    If user is right
    """
        current_letters_guessed.append(letterGuessed)
        if check_word_guess(letterGuessed, randomWord) is False:
            amount_of_times_wrong += 1
        current_letters_right = printWord(current_letters_guessed)
        printLines()
        print_hangman(amount_of_times_wrong)

        # if(randomWord[current_guess_index] == letterGuessed):
        #   print_hangman(amount_of_times_wrong)
        #   """ print word
        #   """
        #   current_guess_index+=1
        #   current_letters_guessed.append(letterGuessed)
        #   printLines()
        # When user was wrong
        # else:
        #   amount_of_times_wrong+=1
        # current_letters_guessed.append(letterGuessed)
        # Update drawing

        # Print the word

    print("Game over! Play again?")
