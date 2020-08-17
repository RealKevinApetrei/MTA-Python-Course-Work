from random import choice
import subprocess
import platform
import os


CWD = os.getcwd()
WORD_FILE = open(CWD + "/words.txt", "r")

WORD_LIST_RAW = list(WORD_FILE.readlines())
WORD_LIST = []

for index, word in enumerate(WORD_LIST_RAW):
    WORD_LIST.append(WORD_LIST_RAW[index].strip("\n"))

NEWLINE = "\n"
TOP_MARGIN = 10
BLANK = "_____"
TOTAL_GUESSES_ALLOWED = 5



def clear_screen():
    subprocess.call("cls" if platform.system() == "Windows" else "clear")


def print_top_margin():
    print(NEWLINE * TOP_MARGIN)


def update_correct_letters(guessed_letter, selected_word, previous_state_of_guesses):
    new_state = list(previous_state_of_guesses)

    if guessed_letter in selected_word:  # If letter correct
        for index, char in enumerate(selected_word):
            if char == guessed_letter:
                new_state[index] = char

    return new_state


def have_won(letters_of_word):
    return not None in letters_of_word


def have_lost(number_of_incorrect_guesses):
    return number_of_incorrect_guesses >= TOTAL_GUESSES_ALLOWED


def done(letters_of_word, number_of_incorrect_guesses):
    if have_won(letters_of_word):
        return True

    if have_lost(number_of_incorrect_guesses):
        return True

    return False



def print_letters_or_blanks(letters_of_word):
    print(" ".join(letter if letter is not None else BLANK
                   for letter in letters_of_word))


def take_letter_guess():
    guess = input("Guess a letter: >>> ")

    if len(guess) > 1:
        return guess[0].lower()
    else:
        return guess.lower()


def print_score_board(score):
    guesses_left = TOTAL_GUESSES_ALLOWED - score

    print("""
Incorrect Guesses: {}
Guesses Left: {}
    """.format(score, guesses_left))


def print_win_banner(selected_word):
    banner = """
    ***************************************************************************
    **********                                                       **********
    **********                                                       **********
    **********                      WIN!!!!!                         **********
    **********                  YOU GUESSED: {}                      **********
    **********                                                       **********
    ***************************************************************************
    """.format(selected_word)

    print(banner)

def print_lose_banner(selected_word):
    banner = """
    ***************************************************************************
    **********                                                       **********
    **********                                                       **********
    **********                     YOU LOSE!!!!!                     **********
    **********                 YOU DID NOT GUESS: {}                 **********
    **********                                                       **********
    ***************************************************************************
    """.format(selected_word)

    print(banner)


def main():  # Main Function
    selected_word = choice(WORD_LIST)  # Random Word
    letters_of_word = [None] * len(selected_word)  # Unknown Letters in word.
    number_of_incorrect_guesses = 0 # Incorrect guesses

    while not done(letters_of_word, number_of_incorrect_guesses):  # Game Loop
        clear_screen()
        print_top_margin()
        print_letters_or_blanks(letters_of_word)
        print_score_board(number_of_incorrect_guesses)

        letter = take_letter_guess()
        letters_of_word = update_correct_letters(letter, selected_word, letters_of_word)

        if letter not in selected_word:
            number_of_incorrect_guesses += 1

    clear_screen()
    print_top_margin()

    if have_won(letters_of_word):
        print_win_banner(selected_word)

    if have_lost(number_of_incorrect_guesses):
        print_lose_banner(selected_word)

    finished = input("Press ENTER to end or type anything to play again: >> ")

    print(f"'{finished}'")

    if finished != "":
        main()

    clear_screen()


if __name__ == "__main__":  # If the acutal file is run...
    main()  # run main() function
