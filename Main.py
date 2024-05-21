import random

def getSillyGreeting():
    num = random.randint(1,3)
    match num:
        case 1:
            return 'you silly person you!\n'
        case 2:
            return 'you nob head you!\n'
        case 3:
            return 'you flapjack you!\n'
        case _:
            return ''

def Greeting():
    name = input("What is your name?\n")
    print("Hello, " + name + " " + getSillyGreeting())

def Guess_a_number():
    guess = input("Guess a number between 1-5.\n>")
    if guess == f'{random.randint(1,5)}':
        print("Correct!")
        Guess_a_number()
    elif guess != "Quit":
        print("WRONG!")
        Guess_a_number()
    else :
        print("Okay, quitter!\n")

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