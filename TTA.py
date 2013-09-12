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
sleep1 = 0
sleep3 = 0
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

#Start of game with wake up sequence
print"Your alarm clock goes off, it is 6:47 a.m."
print"You think you yourself, why did that go off so early?"
print"Work starts at 8:30 a.m., you have about an hour to get ready."
move = raw_input("You turn over and see your alarm clock, do you (hit snooze or get up) ")
stringit(move)
lowerit(move)
#Starting main if block, see 'example structure.py' for better examples
if wake_up_is_right(move) == "correct": 
    print"You stand up, and walk towards the bathroom door"
elif wake_up_is_right(move) == "wrong":
    print"You lean over, and hit snooze on your alarm clock"
    print"As you hit snooze, your arms falls off"
    print"You bleed to death and die."
    print"You are now dead"
    blank = raw_input("Press Enter to close...")
    sys.exit()
else:
    print"Error (420-1), was your spelling right?"
    blank = raw_input("Press Enter to close...")
    sys.exit()
print" "

#Start of bathroom sequence
print"After stumbling towards the bathroom door, you are confronted with an issue"
move = raw_input("Do you (open or keep closed)? ")
if open_is_right(move) == "correct":
    print"You open the door, and move into the bathroom uneventfully"
elif open_is_right(move) == "wrong":
    print"You run away and fall down your stairs breaking your neck"
    print"You live in a 1 story no basement house"
    print"You are dead"
    blank = raw_input("Press Enter to close...")
    sys.exit()
else:
    print"Error (420-2), was your spelling right?"
    blank = raw_input("Press Enter to close...")
    sys.exit()    
print" "

#Part 2 of bathroom sequence
print"After entering the bathroom, you notice your toothbrush"
print"You pick up your toothbrush"
move = raw_input("You ponder, then decide to (pick up or leave there) ")
if leavethere_is_right(move) == "correct":
    print"You notice that the toothbrush has bird poop on it, and leave it there"
elif leavethere_is_right(move) == "wrong":
    print"You start to brush your teeth, everything is fine"
    print"You continue through your day as normal"
    print"Months later, you die of bird flu"
    print"You are dead"
    blank = raw_input("Press Enter to close...")
    sys.exit()    
else:
    print"Error (420-3), was your spelling right?"
    blank = raw_input("Press Enter to close...")
    sys.exit()
print" "

print"Temporary end"
time.sleep(sleepn1)

        
    