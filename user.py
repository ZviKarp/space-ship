import keyboard
def press(c):#gets the direction in which the person is moving, and checks if the user wants to change it
    if keyboard.is_pressed('w'):
        return 'u'
    elif keyboard.is_pressed('s'):
        return 'd'
    elif keyboard.is_pressed('d'):
        return 'r'
    elif keyboard.is_pressed('a'):
        return 'l'
    return c
def Input(text):
    try: 
        return input(text)
    except:
        print ("Numbers Only! Try Again")
        return Input(text)
def Print(brd):#prints a matrix in the form of text 
    text = ""
    for row in brd:
        for unit in row:
            text += unit
        text += "\n"
    print (text)