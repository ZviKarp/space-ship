import keyboard
def press(c):
    if keyboard.is_pressed('w'):
        return 'w'
    elif keyboard.is_pressed('s'):
        return 's'
    elif keyboard.is_pressed('d'):
        return 'd'
    elif keyboard.is_pressed('a'):
        return 'a'
    return c
def Input(text):
    try: 
        return input(text)
    except:
        print ("Numbers Only! Try Again")
        return Input(text)
def Print(brd):
    text = ""
    for row in brd:
        for unit in row:
            text += unit
        text += "\n"
    print text