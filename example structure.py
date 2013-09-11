from TTA import all

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
    blank = raw_input("Press Enter to close...")
    sys.exit()
else:
    print"Fatal Error (420-1), was your spelling wrong?"
    blank = raw_input("Press Enter to close...")
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
    blank = raw_input("Press Enter to close...")
    sys.exit()
else:
    print"Fatal Error (420-2), was your spelling wrong?"
    blank = raw_input("Press Enter to close...")
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
    blank = raw_input("Press Enter to close...")
    sys.exit()
else:
    print"Fatal Error (420-3), was your spelling wrong?"
    blank = raw_input("Press Enter to close...")
    sys.exit()
    
#Temp End
print"Time freezes, and waits forever"
blank = raw_input("Press Enter to close...")
sys.exit()