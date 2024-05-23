import random

# mad lib function
    # get mad lib file object from madlib.txt
    # read lines from file
    # create user input variable that will be a list
    # loop over madlib lines
        # skip even indexed lines (remember the lines will be 0 index), so, 0, 2, 4, etc
        # for each odd indexed line
            # use the line as a prompt to get input from the user and add it to the list
    # loop over the madlib a second time
        # if the index is even 
            # print from the madlib line list
        # if the index is odd
            # print the next item from the user input variable that is also a list

'''
    For this one you'll need to google
        modulo in python to find even odd
        how to 'access' items in a list by index
        how to loop over a list
        python list pop
        
    Output should look something like:

    There once was a
    frog
    who liked to eat
    pancakes
    so much that she would
    run
    every day. Until, one day a
    tenticle
    came
    squirming
    all the way from
    Kansas
    to take it all away.
'''

# mad lib 2 function. This one is bit trickier but should make for cleaner code and better file format for longer madlibs.
    # get madlib file object from madlib2.txt
    # read the entire file into one long string.
    # use regex to find all the {{PROMPT}} patterns in the madlib.txt file and store them in a list
    # use regex to split the big string representing all the text in the file by each {{PROMPT}} in the file so that it becomes a list or array of strings
    # loop over the split list of strings alternating between showing a string for the split list and a string from the {{PROMPS}} gatherd previously from the list.

'''
    For this one you'll need to google
        regex in python
        how to split a list using regex
        how to parse regex matches out of a string (hopefully into an array or list)
        how to "access" an item an a list
        how to loop over a list
        python list pop
'''

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
    userInput = input("Pick a game.\n-\tGuesser.\n-\tQuit.\n\n>") # <- add MadLib to the prompt
    match userInput:
        case "Guesser":
            Guess_a_number()
            menu()
        case "Quit":
            print("Thanks for playing!")
        # add a case for the madlib
        case _:
            print("Pick a game.")
            menu()

Greeting()
menu()