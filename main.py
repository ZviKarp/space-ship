import keyboard 
import time
from user import Input,Print,press
from game import gen_rock,rock_gen
from game import move_lasers,move_rocks
from bordm import con,insert_rock,insert_ship
from moves import move_right,move_left,move_up,move_down
height = 20
width =  40
brd = []
ship = [(width-1)/2,(height-2)] #ship rules: cannot be less than 1 away from edge (half of the ship is to the right of it's actual location) (both edges)
speed = float(Input("Please enter the speed of the game 'higher number-slower game' "))
c = " "
#rocks = [[(width/2),(height/2)]]
rocks = []
rocket_moves = 2#per rock move
rock_move = 2#per rock regeneration

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
def las(brd,height,width):
    for c in range(width):
        brd[height-1][c] = '|'
    return 0
#time.sleep(5)
brd = con(ship,height,width,rocks)
while True:
    for i in range(rock_move):
        time.sleep(speed/100)
        for l in range(rocket_moves):
            c = press(c)
            if keyboard.is_pressed('r'):
                las(brd,height,width)
            brd = move(ship,height,width,rocks,brd,c)
            move_lasers(brd,height,width)
            insert_ship(brd,ship)
            c = " "
        if brd == False:
            print ("You Lost!")
            exit() 
        Print(brd)
        if move_rocks(brd,height,width) == False:#moves rocks
            print "haah"
            print ("You Lost!")
            exit()
    
    insert_rock(brd,rock_gen(brd,height,width))
print ("Was a great game")