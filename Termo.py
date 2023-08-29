import random
from colorama import Back

global win
global tries
global rightL
global rightLP
global guessed
global stopPlaying
global lettersGuess
global lettersChosenWord
global chosenWord


# declaring some variables
def clr_var():
    global win
    global tries
    global rightL
    global rightLP
    global guessed
    global stopPlaying
    global lettersGuess
    global lettersChosenWord
    global chosenWord
    win = False
    tries = 0
    rightL = set()
    rightLP = ['_', '_', '_', '_', '_']
    guessed = 0
    stopPlaying = False
    lettersGuess = list()
    lettersChosenWord = list()
    chosenWord = ""


clr_var()


def slots():
    for i in range(0, 5):
        # Cinza
        if lettersGuess[i] not in lettersChosenWord:
            print(Back.BLACK + f' {lettersGuess[i]} ' + Back.RESET, end=" ")

        # Amarelo
        elif lettersGuess[i] == lettersChosenWord[i]:
            print(Back.GREEN + f' {lettersGuess[i]} ' + Back.RESET, end=" ")

        # Verde
        else:
            print(Back.YELLOW + f' {lettersGuess[i]} ' + Back.RESET, end=" ")
    print("")


while stopPlaying == False:
    clr_var()
    words = ["sagaz", "tonto", "perto", "lerdo", "jeito", "negro", "adeus",
             "burro", "longo", "termo", "sutil", "ideia", "tempo", "morto",
             "causa", "dever", "culto", "forte", "denso", "coisa", "falar"]
    # Generate a random index to pick a random number inside the Word list
    indChosenWord = random.randint(0, len(words))
    # Pick the random word
    chosenWord = words[indChosenWord]
    chosenWord = chosenWord.upper()
    lettersChosenWord = list(chosenWord)

    # print(f'The chosen word is: {chosenWord}')
    while guessed < 5 and win == False and tries < 6:
        # print the slots
        if tries > 0:
            slots()
        # take the user's input
        wordGuess = input("Enter guess: ")
        # make the letters all caps and separate them in a list
        wordGuess = wordGuess.upper()
        lettersGuess = list(wordGuess)
        # check whether the guess is 5 lettered
        if len(wordGuess) == 5:
            for c1 in range(0, 5):
                # check whether each letter of the guess is equal to each letter of the word
                if lettersGuess[c1] == lettersChosenWord[c1]:
                    rightLP[c1] = lettersGuess[c1]
                    rightL.add(lettersGuess[c1])
                elif lettersGuess[c1] in lettersChosenWord:
                    rightL.add(lettersGuess[c1])
            # update counters
            guessed = guessed + 1
            tries = tries + 1
        else:
            print("You must input a 5 letter word")
        if rightLP == lettersChosenWord:
            win = True
    if tries < 6 and win == True:
        slots()
        print("You Win!")
    else:
        slots()
        print("You Lose.")
        print(f"The word was {chosenWord.lower()}")
    SPCheck = 0
    while SPCheck == 0:
        stopPlaying = input("Do you want to stop playing? (y/n)\n")
        stopPlaying = stopPlaying.lower()
        if stopPlaying == 'y':
            stopPlaying = True
            SPCheck = 1
        elif stopPlaying == 'n':
            win = False
            tries = 0
            rightL = set()
            rightLP = ['_', '_', '_', '_', '_']
            guessed = 0
            stopPlaying = False
            SPCheck = 1
        else:
            print("Invalid answer")
"""
"""
