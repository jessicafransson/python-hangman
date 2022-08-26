import random
"""from words import word_list"""
MAX_TURNS = 6
game_running = True
wordDictionary = ["apartment", "house", "flowers", "diamonds", "python",
                  "javascript", "singer", "music",
                  "developer", "system", "book", "movie", "renovation",
                  "display", "credit", "collection", "podcast"]

"""
Choose a random word
"""


def print_hangman(wrong):
    """Get the symbol of hangman displayed when wrong guesses are made"""
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


while(game_running):
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

    while (amount_of_times_wrong != MAX_TURNS and
           current_letters_right != lenght_of_word_to_guess):
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
        print("Remaining guesses = {}".format(MAX_TURNS -
                                              amount_of_times_wrong))
        print("Correct guesses = {}".format(current_letters_right))
        if current_letters_right >= len(randomWord):
            print("\n\n You won! \n\n")
            break
        elif amount_of_times_wrong >= MAX_TURNS:
            print("\n\n You lost! The word was '" + randomWord +
                  "', better luck next time!\n")

    keep_playing = input("\n Play again? (y/n) ")

    if keep_playing in ['y', 'yes', 'ok', 'okay']:
        game_running = True
    else:
        game_running = False


print("You choose no, game over!")
