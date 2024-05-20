import random

# define a function named 'getSillyGreeting'
    # use the random.randint(1,2) function to get a random number between 1 and 2 and store it in a variable named 'num'
    # open a switch statement with the 'match' keyword
        # handle the case for 1
            # return some silly greeting string
        # handle the case for 2
            # return some other silly greeting string

# Here's an incomplete example of the 'getSillyGreeting' function
def getSillyGreeting():
    num = {random.randint(1,3)} # <- use the random library to get a random number
    match num:
        case 1:
            return 'you silly person you!' # <- change the silly greeting if you want
        case 2:
            return 'you nob head you!' # <- some other silly greeting
        # add more cases if you want
        case 3:
            return 'you flapjack you!' # <- some default silly greeting

def Greeting():
    name = input("What is your name?\n")
    print("Hello, " + name + getSillyGreeting) # <-- call the getSillyGreeting function here instead of the "literal string", ", you silly person you"

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