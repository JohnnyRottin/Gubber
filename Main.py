import random

def Greeting():
    name = input("what is your name?\n")
    print("Hello, " + name + ", you silly person you!")

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