# Main file which should handle all the input and display for now
# Nothing really will be split up until much later
# Most of the questions and such that you see will be filler for now.
# I'll probably also forget to delete the above statement once the story starts
# Written by Moomasterq :)

from basicfunc import *
import time
import sys

#Starts the story and asks for name
name = raw_input("What is your name? ")
##Uses the stringit function which makes the variable a string, which in this case is a name
stringit(name)
print"Hello " + name + ", you are about to embark on a journey, get ready"

#Timer, probably a better way to do this, but too lazy to do that, and enjoy doing this.
#Disabled the timers for testing purposes, no need to wait so long for it.
time.sleep(0)
print"5..."
time.sleep(0)
print"4..."
time.sleep(0)
print"3.."
time.sleep(0)
print"2.."
time.sleep(0)
print"1.."
time.sleep(0)
print"Why was there a loading screen in a python game? No clue, just go with it."
time.sleep(1)
##Adds a space between lines
print" "

#Moving along into actual award winning gameplay
move = raw_input("You see a cave, it splits, which way do you head? (Left or Right) ")
##Adds a space between the lines
print" "
##Makes move var into a string and lowercase for if block
stringit(move)
lowerit(move)
if left_is_right(move) == "correct":
    #Sets up text for continuing
    print"You continue through the cave, and find a door. You approach the door."
elif left_is_right(move) == "wrong":
    #Sets up text for being dead
    print"You trip on a ladybug, fall into a cactus, and die."
    time.sleep(5)
    sys.exit()
else:
    print"Fatal Error (420), was your spelling wrong?"
    time.sleep(2)
    sys.exit()
    
#Moving onto the next part of the test story
print"As you move towards the door, you find a key."
move = raw_input("Do you pick up the key or leave it there? (Pick up or Leave there) ")
print" " #Another space
stringit(move)
lowerit(move)
if pickup_is_right(move) == "correct":
    print"You bend over to pick up the key, and a giant hammer misses your head."
    print "You then stand back up."
elif pickup_is_right(move) == "wrong":
    print"A giant hammer aims for your head and completely misses you."
    print"As you breath deeply after your near death experience you stagger backwards."
    print"As you stagger backwards you trip over a ladybug and fall into a cactus."
    print"You are now dead."
    time.sleep(10)
    sys.exit()
else:
    print"Fatal Error (420), was your spelling wrong?"
    time.sleep(2)
    sys.exit()
    
print"Over for now"


