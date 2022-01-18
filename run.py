"""
import random words for generating
random word choice for user.
"""
import random
import string  # ???
from words import words   # takes words from words.py


def get_valid_word(words):  # define function and pass it a list of words
    word = random.choice(words)  # variable 'word' w/ assigned value.
    while '-' in word or ' ' in word:
        word = random.choice(words)  # keep iterating until not True.

    return word.upper()


def hangman():   # record letters correctly guessed and validity of answer/s.
    word = get_valid_word(words)
    word_letters = set(word)  # variable to save all letters in a word as a set
    alphabet = set(string.ascii_uppercase)
    used_letters = set()  # what user has guessed

    lives = 7


# User input
    while len(word_letters) > 0 and lives > 0:    # letters used
        # ".join" turns list into interval/string. ("a", "b", "c" --> "a b c")
        print('You have', lives, 'lives left and used these letters:', ' '.join(used_letters))

        # current word ( ie. W - R D)
        word_list = [letter if letter in used_letters else '-' for letter in word]
        print('Current word: ', ' '.join(word_list))

        user_letter = input('Guess a letter or word: ').upper()
        if user_letter in alphabet - used_letters:
            used_letters.add(user_letter)
            if user_letter in word_letters:
                word_letters.remove(user_letter)
                print(' ')

            else:
                lives = lives - 1  # takes life if wrong
                print('\nYour letter,', user_letter, 'is not in the word.')
# if letter just enetered in used_letters, invalid as already used. 
        elif user_letter in used_letters:
            print('You already used that character, guess again.')

        else:
            print('Invalid choice - try again using only letters.')
    
    # iterates while length of word is greater than zero***
    if lives == 0:
        print('You died, sorry. The word was', word)
    else: 
        print('YAY! You guessed the word', word,'!!')


if __name__ == '__main__':
    hangman()