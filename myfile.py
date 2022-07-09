import io
from random import randint, random

global words
global ques
global l 

rand = 0

def read_file(rand):
    obj= io.open("countries.txt" , "r", encoding= 'utf-8')
    words = obj.read().splitlines()
    obj.close()
    return words[rand]


def game():
    rand = randint(1,196)
    game.country = read_file(rand)
    temp = list(game.country)
    l = len(temp)    
    for i in range(l):
        blankprint = randint(1, i+1)
        if(blankprint==i):
            if game.country[i] == ' ':
                temp[i] = game.country[i]
            else:
                temp[i] = ' _ '
        else:
            temp[i] = game.country[i]
        temp[2] = ' _ '
    game.ques = str()
    for i in range(l):
        game.ques = game.ques+temp[i]
    return (game.ques , l)
    
def check(guess, quess):
    global score
    score = 0
    still_guessing =True
    attempt = 0
    quess = game.country
    
    while still_guessing and attempt<3:
        guess = input()
        if guess.lower() == quess.lower():
            print("Bingo!")
            score = score +10
            still_guessing = False
        else:
            if guess.lower()!= quess.lower():
                attempt = attempt + 1
                score = score-2
                print("Oops! Try again")
            if attempt==3:
                print("The correct answer is: ", game.country)
    print("Score = ", score, '/10')


def ans():
    print("guess the country:")
    game()
    print(game.ques)
    guess = str()
    check(guess, game.ques)
    
ans()
