"""
import random words for generating
random word choice for user.
"""
import random
from words import words   # takes words from words.py

"""
import random words and copy/paste list of words
from google in separate python file. 
"""


def get_valid_word(words):  # define function and pass it a list of words
    word = random.choice(words)   # variable 'word' w/ assigned value 
    while '-' in word or ' ' in word:
        word = random.choice(words)

    return word