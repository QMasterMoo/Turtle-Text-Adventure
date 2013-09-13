# Main file which should handle all the input and display for now
# Nothing really will be split up until much later
# Most of the questions and such that you see will be filler for now.
# I'll probably also forget to delete the above statement once the story starts
# Written by Moomasterq :)

from basicfunc import *
import time
import sys
from random import *

#Sleep countdown timers, change to 0 for testing
sleepn1 = -1
sleep1 = 0
sleep3 = 0
sleep5 = 5
sleep10 = 10
sleep20 = 20

#Passcode var
pc = "0"

#Defines blank variable for no reason other than caution
blank = "doesn't matter"

#Attempt at starting a menu (going to be a long one, going to be a lot of things)
#Nothing is really going to change until I try to get my ideas written
print"Welcome to Turtle-Text-Adventure"
#Defines blank variable for no reason other than caution
blank = "doesn't matter"
menu_correct = False
 
print" "
#Starts menu module
#Dom rewrote menu function, and added some spacing
while not menu_correct:
    print"What would you like to do?"
    print" "
    menu = raw_input("Your options are: 'start game' and 'how to play': ")
    if menufunc(menu) == "starting game":
        print" "
        print"The game is now starting......."
        print" "
        menu_correct = True
        time.sleep(sleep1)
    elif menufunc(menu) == "how to play":
        print" "
        print"You simply respond to statements and questions with one of the options in the  parentheses."
        print"If the question/statement is \"Which way do you choose? (left or right)\" you     would respond with either 'left' or 'right (without parenthesis)"
        print" "
        print"You will be told if your answer is right or wrong with a short story that will  either end the game if its wrong or continue it if it is correct"
        print" "
        print"There are short timers that will allow for you to read the wrong answers before closing and error messages"
        print" "
        print" "
    #Variable that is random that will wait for enter to continue
        menu_correct = True
        blank = raw_input("Press enter to continue to game start... ")
        print" "
    elif menufunc(menu) == "passcode":
        pc = raw_input("Enter passcode here: ")
        stringit(pc)
        print" "
        menu_correct = True
#Error message, game continues.
    else:
        print"You did not enter a valid menu choice. Please choose again."
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
print" "


#While Variable for the while block
#If it's false, it will continue to the story, but if true it will blow through it until the game changes it again to false
#This is the basis of a code based password system
#Block 1
wvar = False
if pc == "1":
    print"Starting at block 1"
    print" "
    pc = "0"
elif pc == "0":
    print" "
else:
    wvar = True
    
while not wvar:
    #Start of game with wake up sequence
    print"Your alarm clock goes off, it is 6:47 a.m."
    print"You think to you yourself, why did that go off so early?"
    print"Work starts at 8:30 a.m., you have about an hour to get ready."
    move = raw_input("You turn over and see your alarm clock, do you (hit snooze or wake up) ")
    #Starting main if block, see 'example structure.py' for better examples
    if wake_up_is_right(move) == "correct": 
        print"You stand up, and walk towards the bathroom door"
        wvar = True
    elif wake_up_is_right(move) == "wrong":
        print"You lean over, and hit snooze on your alarm clock"
        print"As you hit snooze, your arms falls off"
        print"You bleed to death and die."
        print"You are now dead"
        blank = raw_input("Press Enter to close...")
        sys.exit()
    else:
        print"Error (420-1), was your spelling right? Please enter a valid choice."
        blank = raw_input("Press Enter to continue...")
        print" "


#Block 2
wvar = False
if pc == "2":
    print"Starting at block 2"
    print" "
    pc = "0"
elif pc == "0":
    print" "
else:
    wvar = True

while not wvar:
    #Start of bathroom sequence
    print"After stumbling towards the bathroom door, you are confronted with an issue"
    move = raw_input("Do you (open or keep closed)? ")
    if open_is_right(move) == "correct":
        print"You open the door, and move into the bathroom uneventfully"
        wvar = True
    elif open_is_right(move) == "wrong":
        print"You run away and fall down your stairs breaking your neck"
        print"You live in a 1 story no basement house"
        print"You are dead"
        blank = raw_input("Press Enter to close...")
        sys.exit()
    else:
        print"Error (420-2), was your spelling right? Please enter a valid choice."
        blank = raw_input("Press Enter to continue...")  
        print" "


#Block 3
wvar = False
if pc == "3":
    print"Starting at block 3"
    print" "
    pc = "0"
elif pc == "0":
    print" "
else:
    wvar = True
    
while not wvar:
    move = raw_input("Walking in the door, you notice your toothbrush on the sink, do you (pick up or leave there)? ")
    if leavethere_is_right(move) == "correct":
        print"You notice that the toothbrush has bird poop on it, and leave it there"
        wvar = True
    elif leavethere_is_right(move) == "wrong":
        #System for more than one option using random numbers
        rint = random()
        #Makes it option A 25% of the time, and B 75% of the time
        if rint > 0 and rint < .25:
            print"You start to brush your teeth, everything is fine"
            print"You continue through your day as normal"
            print"Months later, you die of bird flu"
            print"You are dead" 
            blank = raw_input("Press Enter to close...")
            sys.exit()  
        else:
            print"You look in the mirror and notice you are a turtle"
            print"Turtles have no teeth"
            print"You accidentally ingest all your toothpaste and die"
            print"You are dead"
            blank = raw_input("Press Enter to close...")
            sys.exit()
    else:
        print"Error (420-3), was your spelling right? Please enter a valid choice."
        blank = raw_input("Press Enter to continue...")
        print" "
print" "


#Block 4
wvar = False
if pc == "4":
    print"Starting at block 4"
    print" "
    pc = "0"
elif pc == "0":
    print" "
else:
    wvar = True
      
while not wvar:
    #Part 3 of bathroom sequence
    print"Being disgusted with the toothbrush, you notice the shower and a box of kellogs brand pop tarts"
    move = raw_input("What do you want to do with the shower (turn on or keep off)? ")
    if keep_off_is_right(move) == "correct":
        print"You ignore the shower, and continue searching"
        wvar = True
    elif keep_off_is_right(move) == "wrong":
        print"You turn on the shower, and get in"
        print"After washing off, you die"
        print"You are now dead"
        blank = raw_input("Press Enter to close...")
        sys.exit()
    else:
        print"Error (420-4), was your spelling right? Please enter a valid choice."
        blank = raw_input("Press Enter to continue...")   
        print" "
print" " 
    
print"Temp end"
blank = raw_input("Press Enter to close...")   
sys.exit()


        
    