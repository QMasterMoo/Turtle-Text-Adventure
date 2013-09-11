# Main file which should handle all the input and display for now
# Nothing really will be split up until much later
# Most of the questions and such that you see will be filler for now.
# I'll probably also forget to delete the above statement once the story starts
# Written by Moomasterq :)

from basicfunc import *
import time
import sys

#Sleep countdown timers, change to 0 for testing
sleepn1 = -1
sleep1 = 1
sleep3 = 3
sleep5 = 5
sleep10 = 10
sleep20 = 20

#Defines blank variable for no reason other than caution
blank = "doesn't matter"

#Attempt at starting a menu (going to be a long one, going to be a lot of things)
#Nothing is really going to change until I try to get my ideas written
print"Welcome to Turtle-Text-Adventure"
#print"Please answer all questions with one of the options in the parentheses and check spelling"""
#######Break between temp intro and menu

print"What would you like to do?"
menu = raw_input("Your options are: start game and how to play. ")
stringit(menu)
lowerit(menu)
#Starts menu module
if menufunc(menu) == "starting game":
    print"The game is now starting"
    print" "
    time.sleep(sleep1)
elif menufunc(menu) == "how to play":
    print"You simply respond to statements and questions with one of the options in the parentheses"
    print"If the question/statement is \"Which way do you choose? (left or right)\" you could respond with anything in the parentheses"
    print"You will be told if your answer is right or wrong with a short story that will either end the game if its wrong or continue it if it is correct"
    print"There are short timers that will allow for you to read the wrong answers before closing and error messages"
    #Variable that is random that will wait for enter to continue
    blank = raw_input("Press enter to continue to game start... ")
#Error message, game continues.
else:
    print"An error has occurred in the menu (69-0), the game will start after a 3 second pause"
    print" "
    time.sleep(sleep3)


#Starts the story and asks for name
name = raw_input("What is your name? ")
##Uses the stringit function which makes the variable a string, which in this case is a name
stringit(name)
print"Hello " + name + ", you are about to embark on a journey, get ready"

#Timer, probably a better way to do this, but too lazy to do that, and enjoy doing this.
time.sleep(sleep1)
print"5..."
time.sleep(sleep1)
print"4..."
time.sleep(sleep1)
print"3.."
time.sleep(sleep1)
print"2.."
time.sleep(sleep1)
print"1.."
time.sleep(sleep3)
print"Loading Complete"
time.sleep(sleep3)
##Adds a space between lines
print" "

print"Empty holder space for the 0.0.7 release"
time.sleep(sleepn1)