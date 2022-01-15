"""
Import random dictionary for random word selecton
"""
import random
# these are the libraries used which will generate
# the random words from below list

name = input("Enter Name")
# this is the first step to playing which is required
# in order to get to next step

print(f"Good luck, {name}")

words = ['cereal', 'glacier', 'temperature', 'superior', 'fountain',
                'hobby', 'royalty', 'rebel', 'flourish', 'glow', 'concert',
            'legend', 'massage', 'pleasant', 'elegant']
# this function will pick a word randomly out of the list

word = random.choice(words)
