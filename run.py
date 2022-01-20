import random

# set up the word and hidden list.
words = ['experiment', 'leash', 'me', 'second', 'rehearsal', 'carry',
        'shine', 'great', 'motif', 'intervention', 'shake', 'narrow',
        'bridge', 'story', 'blonde', 'field', 'man', 'rotate', 'disappoint',
        'purpose', 'irony', 'consideration', 'weapon', 'cable', 'governor',
        'enlarge', 'aspect', 'free', 'laser', 'pill']
hidden = []

word = random.choice(words)

for character in words:
    hidden.append("_")

attempts = 0
max_attempts = 5

# loop until either the player has won or lost.
isGameOver = False
while not isGameOver:

    # dislay the current boards, guessed letters and attempts remaining.
    print(f'You have {max_attempts - attempts} attempts ramaining')

    print(f"The current word is: {' '.join(hidden)}")

    print("     ------")
    print("     |    |")
    print("     |    " + ("O" if attempts > 0 else ""))
    print("     |    " + ("/\\" if attempts > 1 else ""))
    print("     |    " + ("|" if attempts > 2 else ""))
    print("     |    " + ("/\\" if attempts > 3 else ""))
    print(" --------")

    # ask the player for a character.
    letterGuessed = input("Please guess a letter: ")
    print("\n\n\n\n")

    if letterGuessed in words:
        # if guessed correct, show all matched letters and print message
        print(f'Nice work, the letter {letterGuessed} is in the word!')
        for i in range(len(word)):
            character = words[i]
            if character == letterGuessed:
                hidden[i] = words[i]
                words[i] = '_'
    else:
        # if guessed wrong, print failure message and incorrect attempts.
        print(f'Unlucky, the letter {letterGuessed} is not in the word.')
        attempts += 1

    # if the player wins print congrats message and stop the looping.
    if (all('_' == char for char in word)):
        print("Congrats, Man! You won!")
        isGameOver = True

    # if player has lost, print fail message and stop loop.
    if (attempts == max_attempts):

        print("Ouch, better luck next time!")
        isGameOver = True
