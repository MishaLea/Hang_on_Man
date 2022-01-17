"""
import random words for generating
random word choice for user.
"""
import random
from words import words   # takes words from words.py
import string  # ???


def get_valid_word(words):  # define function and pass it a list of words
    word = random.choice(words)   # variable 'word' w/ assigned value 
    while '-' in word or ' ' in word:
        word = random.choice(words)  # keep iterating until not True. 

    return word


def hangman():   # record letters correctly guessed and validity of answer/s.
    word = get_valid_word(words)
    word_letters = set(word)  # variable to save all letters in a word as a set
    alphabet = set(string.ascii_uppercase)
    used_letters = set()  # what user has guessed


    # User input 
    user_letter = input("Guess a letter or word: ").upper()
    if user_letter in alphabet - used_letters:
        used_letters.add(user_letter)
        if user_letter in word_letters:
            word_letters.remove(user_letter)

    
    # if letter just enetered in used_letters, invalid as already used. 
    elif user_letter in used_letters:
        print("You already used that character, guess again.")

    else:
        print("Invalid choice - try again using only letters.")


user_input = input("Hang on, Man. Type something to play: ")
print(user_input)