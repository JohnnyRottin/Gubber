import random

def Greeting():
    name = input("What is your name?\n")
    print("Hello, " + name + ", you silly person you!")

def Guess_a_number():
    guess = input("Guess a number between 1-5.\n>")
    if guess == f'{random.randint(1,5)}':
        print("Correct!")
        Guess_a_number()
    elif guess != "Quit":
        print("WRONG!")
        Guess_a_number()
    else :
        print("Okay, quitter!")

def menu():
    userInput = input("Pick a game.\n-\tGuesser.\n-\tQuit.\n\n>")
    match userInput:
        case "Guesser":
            Guess_a_number()
            menu()
        case "Quit":
            print("Thanks for playing!")
        case _:
            print("Pick a game.")
            menu()

Greeting()
menu()