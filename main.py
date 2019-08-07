import keyboard 
from user import Input,Print,press
from game import gen_rock
from bordm import con
height = 20
width =  40
brd = []
ship = [(width-1)/2,(height-1)] #ship rules: cannot be less than 1 away from edge (half of the ship is to the right of it's actual location)
speed = Input("Please enter the speed of the game 'higher number-slower game' ")
c = " "
rocks = [[(width/2),(height/2)]]

def move(ship,height,width,rocks,brd,c):
    
    

while True:
    for i in range(speed):
        c = press(c)
    print (c)
    brd = con(ship,height,width,rocks)
    Print(brd)