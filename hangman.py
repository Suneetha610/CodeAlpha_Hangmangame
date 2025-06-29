import getpass
import os
from colorama import Fore, Style, init
init(autoreset=True)

HANGMAN_PICS = [
    '''
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
    /|\\  |
         |
         |
    =========''', '''
     +---+
     |   |
     O   |
    /|\\  |
    /    |
         |
    =========''', '''
     +---+
     |   |
     O   |
    /|\\  |
    / \\  |
         |
    ========='''
]

def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

def welcome():
    clear_screen()
    print(Fore.CYAN + Style.BRIGHT + "=" * 40)
    print(Fore.MAGENTA + Style.BRIGHT + " WELCOME TO THE HANGMAN GAME ".center(40))
    print(Fore.CYAN + Style.BRIGHT + "=" * 40 + "\n")

def get_secret_word():
    print(Fore.YELLOW + "Player 1, please enter a secret word for Player 2 to guess.")
    word = getpass.getpass("Enter the word (hidden): ").lower()
    clear_screen()
    return word

def display_word(word, guessed_letters):
    display = ""
    for letter in word:
        if letter in guessed_letters:
            display += Fore.GREEN + letter + " " + Style.RESET_ALL
        else:
            display += "_ "
    print("Word:", display.strip())

def play_game():
    welcome()
    word = get_secret_word()
    guessed_letters = []
    tries = 6

    while tries > 0:
        print(Fore.CYAN + HANGMAN_PICS[6 - tries])
        display_word(word, guessed_letters)

        if all(letter in guessed_letters for letter in word):
            print(Fore.GREEN + "\n Congratulations! You guessed the word:", word)
            break

        guess = input(Fore.BLUE + "\nGuess a letter: ").lower()

        if not guess.isalpha() or len(guess) != 1:
            print(Fore.RED + " Please enter a single valid letter.")
            continue

        if guess in guessed_letters:
            print(Fore.YELLOW + "You already guessed that letter.")
        elif guess in word:
            print(Fore.GREEN + " Good job! That letter is in the word.")
            guessed_letters.append(guess)
        else:
            print(Fore.RED + " Wrong guess.")
            guessed_letters.append(guess)
            tries -= 1
            print(Fore.MAGENTA + f" Tries left: {tries}")

        print()

    if tries == 0:
        print(Fore.RED + HANGMAN_PICS[6])
        print(Fore.RED + " Game over! The word was:", word)

play_game()
