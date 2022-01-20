"""
Import random library for
game to choose random words
"""
import random


def hangman():
    list_of_words = ["airplane", "airport", "ajar", "alarm",
                     "alcoholic", "alert", "alike", "alive",
                     "alleged"]
    word = random.choice(list_of_words)
    turns = 10
    guessmade = ''
    valid_entry = set('abcdefghijklmnopqrstuvwxyz')

    while len(word) > 0:
        main_word = ""

        # letter is a new variable
        for letter in word:
            if letter in guessmade:
                main_word = main_word + letter
            else:
                main_word = main_word + "_ "

        if main_word == word:
            print(f"{main_word}")
            print("You won")
            break

        print(f"Guess the word {main_word}")
        guess = input()

        if guess in valid_entry:
            guessmade = guessmade + guess
        else:
            print("Enter valid character")
            guess = input()

        if guess not in word:
            turns = turns - 1

            if turns == 9:
                print("9 turns left")
                print("-----------------")
            if turns == 8:
                print("8 turns left")
                print("-----------------")
                print("        0        ")
            if turns == 7:
                print("7 turns left")
                print("-----------------")
                print("        0        ")
                print("        |        ")
            if turns == 6:
                print("6 turns left")
                print("-----------------")
                print("        0        ")
                print("        |        ")
                print("       /         ")
            if turns == 5:
                print("5 turns left")
                print("-----------------")
                print("        0        ")
                print("        |        ")
                print("       / \       ")
            if turns == 4:
                print("4 turns left")
                print("-----------------")
                print("      \ 0        ")
                print("        |        ")
                print("       / \       ")
            if turns == 3:
                print("3 turns left")
                print("-----------------")
                print("      \ 0 /      ")
                print("        |        ")
                print("       / \       ")
            if turns == 2:
                print("2 turns left")
                print("-----------------")
                print("        |        ")
                print("      \ 0 /      ")
                print("        |        ")
                print("       / \       ")
            if turns == 1:
                print(" only 1 turn left! Hang on, Man - You got this!")
                print("-----------------")
                print("       ___       ")
                print("        |        ")
                print("      \ 0 /      ")
                print("        |        ")
                print("       / \       ")
            if turns == 0:
                print(". . . . . . . . . . .")
                print("Sorry, Man. You lose!")
                print("Better luck next time!")
                break


name = input("Welcome to 'Hang on, Man!' Enter your name here -> ")
print(f"Welcome {name}!")
print(". . . . . . . . . . . . ")
print("Try to guess the word - HINT! Start with vowels.")
hangman()
