from rules import safe_surround
from bordm import remove_ship,insert_ship
#these functions move the ship
def move_right(ship,height,width,rocks,brd,c):#moves the space-ship one block over to the right
    remove_ship(brd,ship)
    if ship[0] == width-2:#if there isn't enough room to have an extra block between the ship and the border after moving right
        insert_ship(brd,ship)
        return ship
    elif safe_surround(brd,ship[1],ship[0]):
        ship[0] += 1
        insert_ship(brd,ship)
        return ship 
    else:
        return False
def move_left(ship,height,width,rocks,brd,c):
    remove_ship(brd,ship)
    if ship[0] == 1 :#if after we move it there would be extra room to the left to have one more block between teh ship and the border 
        insert_ship(brd,ship)
        return ship
    elif safe_surround(brd,ship[1],ship[0]):
        ship[0] += -1
        insert_ship(brd,ship)
        return ship
    else:
        return False
def move_up(ship,height,width,rocks,brd,c):
    remove_ship(brd,ship)
    if ship[1] == 1:#if we move the whip up there wouldn't be any room to go up anymore 
        insert_ship(brd,ship)
        return ship
    elif safe_surround(brd,ship[1],ship[0]):
        ship[1] += -1
        insert_ship(brd,ship)
        return ship
    else:
        return False
def move_down(ship,height,width,rocks,brd,c):
    remove_ship(brd,ship)
    if ship[1] == height-2 :#can't move down
        insert_ship(brd,ship)
        return ship
    elif safe_surround(brd,ship[1],ship[0]):
        ship[1] += 1
        insert_ship(brd,ship)
        return ship
    else:
        return False
