def con(ship,height,width,rocks):
    brd  = []
    for row in range(height):
        brd.append([])
        for column in range(width):
            brd[row].append(" ")
    brd[ship[1]][ship[0]] = "/"
    brd[ship[1]][ship[0]+1] = "\\"
    for rock in rocks:
        print rock
        print width
        print height
        brd[rock[1]][rock[0]] = "O"
    return brd
