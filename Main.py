import random

def Greeting():
    name = input("what is your name?\n")
    print("Hello, " + name)

def Guess_a_number():
    guess = input("Guess a number between 1-5.\n>")
    if guess == f'{random.randint(1,5)}':
        print("Correct!")
        Guess_a_number()
    elif guess != "quit":
        print("WRONG!")
        Guess_a_number()
    else :
        print("Okay quitter!")

Greeting()
Guess_a_number()