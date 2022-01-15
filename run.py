"""
Import random dictionary for random word selecton
"""
import random
from collections import Counter
# these are the libraries used which will generate
# the random words from below list

name = input("Enter Name: ")
# this is the first step to playing which is required
# in order to get to next step

print(f"Good luck, {name}")


words = ['cereal', 'glacier', 'temperature', 'superior', 'fountain',
         'hobby', 'royalty', 'rebel', 'flourish', 'glow', 'concert',
         'legend', 'massage', 'pleasant', 'elegant']
# this function will pick a word randomly out of the list

word = random.choice(words)

if __name__ == '__main__':
    print("Take a guess - first hint, start with the vowels")

    for i in word:
        print('-', end='')
    print()

    playing = True
    # list for storing the letters guessed by the player
    lGuessed = ''
    chances = len(word) + 2
    correct = 0
    flag = 0
    try:
        # flag updated when guessed correctly
        while (chances != 0) and flag == 0:
            print()
            chances -= 1

            try:
                guess = str(input("Enter letter to guess: "))
            except KeyboardInterrupt():
                print("Enter only one letter!")
                continue
            # guessing invalid answers
            if not guess.isalpha():
                print("only enter a letter. E.g. a,b,c etc...")
                continue
            elif len(guess) > 1:
                print("Enter only 1 letter at a time")
                continue
            elif guess in lGuessed:
                print("You have already used that letter")
                continue

            # if guessed correctly
            if guess in word:
                k = word.count(guess)  # k stores the number of times
                # the guessed letter occurs in the word
                for _ in range(k):
                    lGuessed += guess  # The guess letter is added
                    # as many times as it occurs
            for char in word:
                if char in lGuessed and (Counter(lGuessed) != Counter(word)):
                    print(char, end='')
                    correct += 1
                # if user has guessed all letters
                elif (Counter(lGuessed) == Counter(word)):
                    # Once the correct word is guessed fully
                    print("The word is: ", end=' ')
                    print(word)
                    flag = 1
                    print("Congrats! You won!")
                    break
                    break
                else: 
                    print('_', end='')

        # If user has used all of his chances
        if chances <= 0 and (Counter(lGuessed) != Counter(word)):
            print()
            print('You lost! Try again..')
            print('The word was {}'.format(word))
        
    except KeyboardInterrupt:
        print()
        print('Bye! Try again.')
        exit()
