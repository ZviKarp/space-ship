def con(ship,height,width,rocks):#creates the brd (matrix with all the content inside) based on 'ship' and 'rocks'
    brd  = []
    for row in range(height):
        brd.append([])
        for column in range(width):
            brd[row].append(" ")
    brd[ship[1]][ship[0]-1] = "/"
    brd[ship[1]][ship[0]] = "|"
    brd[ship[1]][ship[0]+1] = "\\"
    for rock in rocks:
        print rock
        print width
        print height
        brd[rock[1]][rock[0]] = "O"
    return brd

def remove_ship(brd,ship):#removes the ships off the map (from the location given in ship)
    brd[ship[1]][ship[0]] = " "#emptying the ships location
    brd[ship[1]][ship[0]-1] = " "
    brd[ship[1]][ship[0]+1] = " "
    return 0
def insert_ship(brd,ship):#inserts a ship into brd in brd
    brd[ship[1]][ship[0]-1] = "/"
    brd[ship[1]][ship[0]] = "|"#inserting a ship into brd
    brd[ship[1]][ship[0]+1] = "\\"
    return 0
def insert_rock(brd,rock):
    brd[rock[1]][rock[0]] = "O"
    return 0