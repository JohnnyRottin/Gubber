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
    num = 2 # <- use the random library to get a random number
    match num:
        case 1:
            return 'you silly person you!' # <- change the silly greeting if you want
        case 2:
            return '...' # <- some other silly greeting
        # add more cases if you want
        case _:
            return '...' # <- some default silly greeting

def Greeting():
    name = input("What is your name?\n")
    print("Hello, " + name + ", you silly person you!") # <-- call the getSillyGreeting function here instead of the "literal string", ", you silly person you"

def Guess_a_number():
    guess = input("Guess a number between 1-5.\n>")
    if guess == f'{random.randint(1,5)}':
        print("Correct!")
        Guess_a_number()
    elif guess != "quit":
        print("WRONG!")
        Guess_a_number()
    else :
        print("Okay, quitter!")

#define the main function here like...
# def main():
    # Take in user input
    # switch statement with cases
        # case for the guess a number
            # call the gues a number function
        # case for quit
            # call them a quitter and don't call any other function
        # default case
            # say "Invalid option" or something, and call the 'main' function again

# We still call the greeting function...
Greeting()

# but now we also call the main function here like...
# main()