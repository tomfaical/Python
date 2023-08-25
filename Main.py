import random

# declaring some variables
global win
win = False
tries = 0
rightL = set()
rightLP = ['_', '_', '_', '_', '_']
guessed = 0
stopPlaying = False
def slots():
    print(f"{rightLP[0]}{rightLP[1]}{rightLP[2]}{rightLP[3]}{rightLP[4]}")


while stopPlaying == False:
    words = ["sagaz", "tonto", "perto", "lerdo", "jeito", "negro", "adeus",
             "burro", "longo", "termo", "sutil", "ideia", "tempo", "morto",
             "causa", "dever", "culto", "forte", "denso", "coisa", "falar"]
    # Generate a random index to pick a random number inside the Word list
    indChosenWord = random.randint(0, len(words))
    # Pick the random word
    chosenWord = words[indChosenWord]
    lettersChosenWord = list(chosenWord)
    while guessed < 5 and win == False and tries < 6:
        wordGuess = input("Enter guess: ")
        lettersGuess = list(wordGuess)
        if len(wordGuess) == 5:
            for c1 in range(0,5):
                if lettersGuess[c1] == lettersChosenWord[c1]:
                    rightLP[c1]=lettersGuess[c1]
                    rightL.add(lettersGuess[c1])
                elif lettersGuess[c1] in lettersChosenWord:
                    rightL.add(lettersGuess[c1])
            print("the right guesses are " + str(rightL))
            slots()
            guessed = guessed + 1
            tries = tries + 1
        else: print("You must input a 5 letter word")
        if rightLP == lettersChosenWord:
            win = True
    if tries < 6 and win == True:
        print ("You Win!")
    else:
        print("You Lose.")
    stopPlaying = input("Do you want to stop playing? (y/n)\n")
    if stopPlaying == 'y' or stopPlaying == 'Y':
        stopPlaying = True
    elif stopPlaying == 'n' or stopPlaying == 'N':
        win = False
        tries = 0
        rightL = set()
        rightLP = ['_', '_', '_', '_', '_']
        guessed = 0
        stopPlaying = False
