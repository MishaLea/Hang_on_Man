# set up the word and hidden list.
word = list("apple")
hidden = []
for character in word:
    hidden.append("_")

attempts = 0
max_attempts = 4

# loop until either the player has won or lost.
isGameOver = False
while not isGameOver:

    # dislay the current boards, guessed letters and attempts remaining.
    print(f'You have {attempts} attempts ramaining')

    hiddenString = ' '.join(hidden)
    print(f'The current word is: {hiddenString}')
    
    print("     ------")
    print("     |    |")
    print("     |    " + ("O" if attempts > 0 else ""))
    print("     |    " + ("/\\" if attempts > 1 else ""))
    print("     |    " + ("|" if attempts > 2 else ""))
    print("     |    " + ("/\\" if attempts > 3 else ""))
    print(" --------")


    # ask the player for a character.
    letterGuessed = input("Please guess a letter: ")

    if letterGuessed in word:
        for i in range(len  (word)  ):
            character = word[i]
            if character == letterGuessed:
                hidden[i] = word[i]
                word[i] = '_'

    print(hidden)
    print(word)

    # if the player guessed correct, show all matched letters and print message

    # if player guessed wrong, print failure message and incorrect attempts.

    # if the player wins print congrats message and stop the looping.

    # if player has lost, print fail message and stop loop. 