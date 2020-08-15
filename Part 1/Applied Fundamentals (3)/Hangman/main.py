from random import choice
import subprocess
import platform


WORD_LIST = (
    "cheese",
    "apple",
    "orange",
    "banana",
    "pan",
    "fries",
    "cold",
    "hot",
    "boiling",
    "freezing"
)


def main():  # Main Function
    output = ""
    selected_word = choice(WORD_LIST)
    letters_of_word = [None] * len(selected_word)

    # Game Loop
    while True:
        # Clear Terminal Window
        subprocess.call("cls" if platform.system() == "Windows" else "clear")

        print(selected_word)
        print(letters_of_word)

        letter = input("Guess a letter: >>> ")

        output += letter
        if len(output) > 10:
            break
        if letter in selected_word:
            for index, char in enumerate(selected_word):
                if char == letter:
                    letters_of_word[index] = char


    # End of Game
    print("Congratulations! You won with the word: {}".format(output))


if __name__ == "__main__":  # If the acutal file is run...
    main()  # run main() function
