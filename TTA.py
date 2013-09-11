# Main file which should handle all the input and display for now
# Nothing really will be split up until much later
# Most of the questions and such that you see will be filler for now.
# I'll probably also forget to delete the above statement once the story starts
# Written by Moomasterq :)

from basicfunc import *
import time
import sys

sleepn1 = -1
sleep1 = 1
sleep3 = 3
sleep5 = 5
sleep10 = 10
sleep20 = 20


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

#Moving along into actual award winning gameplay
move = raw_input("You see a cave, it splits, which way do you head? (left or right) ")
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
    time.sleep(sleepn1)
    sys.exit()
else:
    print"Fatal Error (420-1), was your spelling wrong?"
    time.sleep(sleepn1)
    sys.exit()
    
#Moving onto the next part of the test story
print"As you move towards the door, you find a key."
move = raw_input("Do you pick up the key or leave it there? (pick up or leave there) ")
print" " #Another space
stringit(move)
lowerit(move)
if pickup_is_right(move) == "correct":
    print"You bend over to pick up the key, and a giant hammer misses your head."
    print "You then stand back up."
elif pickup_is_right(move) == "wrong":
    print"A giant hammer aims for your head and completely misses you."
    print"As you breathe deeply after your near death experience you stagger backwards."
    print"As you stagger backwards you trip over a ladybug and fall into a cactus."
    print"You are now dead."
    time.sleep(sleepn1)
    sys.exit()
else:
    print"Fatal Error (420-2), was your spelling wrong?"
    time.sleep(sleepn1)
    sys.exit()
    
#Moveing onto another part that simply extends the story
print"After narrowly escaping death, you stand back up against better judgment."
move = raw_input("When standing up, you realize you left the key there, do you (pick up or leave there)? ")
#Extra space
print" "
stringit(move)
lowerit(move)
if pickup_is_right(move) == "correct":
    print"You bend over and try to pick up the key. You find that the key is glued to the ground"
    print"As you try to pry it off the ground, the hammer comes back for a second time and narrowly misses your head."
    #Temp sleep
    time.sleep(sleep10)
elif pickup_is_right(move) == "wrong":
    print"The hammer comes back down and hits you in the head. (Seriously, it will come back down... eventually)"
    print"You are now dead."
    time.sleep(sleep10)
    sys.exit()
else:
    print"Fatal Error (420-3), was your spelling wrong?"
    time.sleep(sleep3)
    sys.exit()
    
#Temp End
print"Time freezes, and waits for another update"
time.sleep(sleep5)
sys.exit()
    

