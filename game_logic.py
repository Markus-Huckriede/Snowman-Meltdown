import random
from ascii_art import STAGES

WORDS = ["python", "git", "github", "snowman", "meltdown"]
MAX_MISTAKES = len(STAGES) -1


def display_game_state(mistakes, secret_word, guessed_letters):
    print(STAGES[mistakes])
    display_word = ""
    for letter in secret_word:
        if letter in guessed_letters:
            display_word += letter + " "
        else:
            display_word += "_ "
    print("Word: ", display_word)
    print("\n")


def get_random_word():
    return WORDS[random.randint(0, len(WORDS) - 1)]


def check_win(secret_word, guessed_letters):
    return all(letter in guessed_letters for letter in secret_word)


def new_game():
    while True:
        ask_for_new_game = input("Wanna play again? (Y/N) ").lower()
        if ask_for_new_game == "y":
            play_game()
            break
        elif ask_for_new_game == "n":
            print("Bye.")
            break
        else:
            print("Please enter Y or N.")


def play_game():
    secret_word = get_random_word()
    guessed_letters = []
    mistakes = 0

    print("Welcome to Snowman Meltdown!")
    display_game_state(mistakes, secret_word, guessed_letters)

    while mistakes < MAX_MISTAKES and not check_win(secret_word, guessed_letters):
        guess = input("Guess a letter: ").lower()

        if len(guess) != 1:
            print("Please enter a single letter.")
            continue

        if guess in guessed_letters:
            print("You already guessed that letter.")
            continue

        guessed_letters.append(guess)

        if guess not in secret_word:
            mistakes += 1
            print(f"Wrong guess. You have {MAX_MISTAKES - mistakes} tries left.")
        else:
            print("Right letter!")

        display_game_state(mistakes, secret_word, guessed_letters)

    if check_win(secret_word, guessed_letters):
        print("Congratulations, you saved the snowman!")
    else:
        print(STAGES[-1])
        print(f"Snowman melted! The word was: {secret_word}")
    new_game()

