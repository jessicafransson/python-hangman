import random

"""from words import word_list"""
MAX_TURNS = 6
game_running = True
word_dictionary = ["apartment", "house", "flowers", "diamonds", "python",
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


def print_word(guessedLetters):
    """ Display the guesses being made and counting
    """
    counter = 0
    right_letters = 0
    for char in random_word:
        if (char in guessedLetters):
            print(random_word[counter].upper(), end=" ")
            right_letters += 1
        else:
            print(" ", end=" ")
        counter += 1
    return right_letters


def print_lines():
    """
    print the correct word
    """
    print("\r")
    for char in random_word:
        print("\u203E", end=" ")


def check_word_guess(guess, word):
    """check if the guessed word is correct or false"""
    if guess in word:
        return True
    return False


"""run the game"""
if __name__ == "__main__":
    while (game_running):
        random_word = random.choice(word_dictionary)
        print("Welcome, let's play hangman!")
        print("________________________________")
        print_hangman(0)
        for x in random_word:
            print("_ ", end="")
        lenght_of_word_to_guess = len(random_word)
        amount_of_times_wrong = 0
        current_guess_index = 0
        current_letters_guessed = []
        current_letters_right = 0
        keep_playing = "no"

        while (amount_of_times_wrong != MAX_TURNS and
            current_letters_right != lenght_of_word_to_guess):

            """prompt user for input"""
            letterGuessed = input("\nGuess a letter: ")

            """
            print whether the guess is correct or false,
            and display the correct word with a wrong guess
            """
            current_letters_guessed.append(letterGuessed)
            if check_word_guess(letterGuessed, random_word) is False:
                amount_of_times_wrong += 1
            current_letters_right = print_word(current_letters_guessed)
            print_lines()
            print_hangman(amount_of_times_wrong)
            print("Remaining guesses = {}".format(MAX_TURNS -
                                                amount_of_times_wrong))
            print("Correct guesses = {}".format(current_letters_right))
            if current_letters_right >= len(random_word):
                print("\n\n You won! \n\n")
                break
            elif amount_of_times_wrong >= MAX_TURNS:
                print("\n\n You lost! The word was '" + random_word +
                    "', better luck next time!\n")

        """choose to reset the game or start again"""
        keep_playing = input("\n Play again? (y/n) ")

        if keep_playing in ['y', 'yes', 'ok', 'okay']:
            game_running = True
        else:
            game_running = False

    """ended game print this"""
    print("You choose no, game over!")
