import keyboard 
import time
from user import Input,Print,press
from game import gen_rock
from game import move_lasers
from bordm import con,insert_rock,insert_ship
from moves import move_right,move_left,move_up,move_down
height = 20
width =  40
brd = []
ship = [(width-1)/2,(height-1)] #ship rules: cannot be less than 1 away from edge (half of the ship is to the right of it's actual location) (both edges)
speed = float(Input("Please enter the speed of the game 'higher number-slower game' "))
c = " "
rocks = [[(width/2),(height/2)]]

def move(ship,height,width,rocks,brd,c):#ship - coordinants of the ship, height and width - of the board, rocks - list of the coordinants of the rocks, brd - matrix with char's resembling what's in that place of the board,c - character resembling in what direction the player is moving 
    if c == "r":
        ship = move_right(ship,height,width,rocks,brd,c)
    elif c == "l":
        ship = move_left(ship,height,width,rocks,brd,c)
    elif c == "u":
        ship = move_up(ship,height,width,rocks,brd,c)
    elif c == "d":
        ship = move_down(ship,height,width,rocks,brd,c)
    if ship == False:
        return False
    else:
        return brd

    

brd = con(ship,height,width,rocks)
while True:
    for i in range(10):
        time.sleep(speed/100)
        
        c = press(c)
        brd = move(ship,height,width,rocks,brd,c)
        move_lasers(brd,height,width)
        insert_ship(brd,ship)
        c = " "
        if brd == False:
            print ("You Lost!")
            break
        
        Print(brd)
    
    insert_rock(brd,gen_rock(brd,height,width))
print ("Was a great game")