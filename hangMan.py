# this is just a small representation of general knowladge in Python 
# I will be making a hangman game that asks the users to guess a letter and find out if it is correct

import random
import time

wordList = ["Abstract","Headphones","watch","dispose","alternator","electricity","constantinople","scapula","tramisu","sculpture"]
emptyList =[]
health = 0

print("Welcome to Hangman !!!")
time.sleep(2)

secretWrd = random.choice(wordList)

print("You get 5 guesses")

for letter in secretWrd:
    emptyList += "_" 
    
print(emptyList)

guess = input("Please Guess a letter ").lower()



game_ovr = False

while not game_ovr:
    guess = input("Please Guess a letter ").lower()
    for position in range(len(secretWrd)):
        letter = secretWrd[position]
        if letter == guess:
            emptyList[position] = letter
    print(emptyList)
    if guess not in emptyList:
        health += 1
        health_nw = 5 - health
        print(f"You get {health_nw} more tries")
        if health >=5:
            print("GAME OVER \n")
            game_ovr = True
            print("correct word was " + secretWrd )
    

    if "_" not in emptyList:
        print("YOU WINN !!!")
        game_ovr = True       