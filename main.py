from pyfiglet import Figlet
from termcolor import colored
import random

# LOGO
Logo = Figlet(font='slant')
print(Logo.renderText('PyWordsGame'))

# Get game word
mainWord = random.choice(open('words.txt').read().split()).strip()

# Start game
print('Try to guess the word')
clientWord = input(">>>")

roundOfGame = 1


def game(mainWord, clientWord, roundOfGame):
    if len(clientWord) != 5:
        print('Input only 5 letter')
        clientWord = input(">>>")
        game(mainWord, clientWord, roundOfGame)
    print(roundOfGame)
    for letter in range(0, 5):
        if clientWord[letter] != mainWord[letter]:
            if mainWord.find(clientWord[letter]) != -1:
                print(colored(clientWord[letter], 'yellow'), end="")
            else:
                print(colored(clientWord[letter], 'red'), end="")
        else:
            print(colored(clientWord[letter], 'green'), end="")
    roundOfGame += 1
    # Win Game
    if clientWord == mainWord:
        print('You win!!!!')
        exit()
    # Lose Game
    if roundOfGame == 6:
        print('You Lose!!!!')
        exit()
    # Recall Fn
    print('\n')
    print('Try to guess the word')
    clientWord = input(">>>")
    game(mainWord, clientWord, roundOfGame)


game(mainWord, clientWord, roundOfGame)
