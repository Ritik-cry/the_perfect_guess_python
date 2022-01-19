# THE PERFECT GUESS game

from random import randint
comp = randint(1,100)
you = None
guess = 0

while(you != comp):
    you = int(input("Enter your guess : "))
    guess += 1
    if you==comp:
        print("You guessed it RIGHT !!!")
    elif you>comp:
        print("You guessed it WRONG !!! Please enter SMALLER NUMBER")
    elif you<comp:
        print("You guessed it WRONG !!! Please enter HIGHER NUMBER")

print(f" *** GUESSES taken to predict RIGHT ANSWER {comp} : '{guess}' ***")    
