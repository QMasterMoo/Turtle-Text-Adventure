#Should handle most of the default functions that will come back throughout


def lowerit(i): #Makes the input lowercase for if blocks
    return i.lower()

def stringit(i): #Makes the input strings for whatever reason
    return str(i)

def left_is_right(i): #Function for making the "Left" direction correct
    if i == "left":
        return "correct"
    elif i == "right":
        return "wrong"
    else:
        return "error (420)"
    

def right_is_right(i): #Function for making the "Right" direction correct
    if i == "left":
        return "wrong"
    elif i == "right":
        return "correct"
    else:
        return "error (420)"

def up_is_right(i): #Function for making the "Up" direction correct
    if i == "up":
        return "correct"
    elif i == "down":
        return "wrong"
    else:
        return "error (420)"
    
def down_is_right(i): #Function for making the "Down" direction correct
    if i == "up":
        return "wrong"
    elif i == "down":
        return "correct"
    else:
        return "error 420"

def pickup_is_right(i): #Function for making the "Pick Up" option correct
    if i == "pick up":
        return "correct"
    elif i =="leave there":
        return "wrong"
    else:
        return "error 420"

def leavethere_is_right(i): #Function for making the "Leave there" option correct
    if i == "pick up":
        return "wrong"
    elif i == "leave there":
        return "correct"
    else:
        return "error 420"