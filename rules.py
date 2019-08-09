def safe_surround(brd,row,column):
    for item in surroundings(brd,row,column):
        if item != " " and item != "|":
            return False
    return True
list1 = [
    [1,2,3],
    [4,5,6],
    [7,8,9]
]

def surroundings(brd,row,column):
    slist = []
    for c in range(column-1,column+2):
        try:
            slist.append(brd[row+1][c])
        except:
            pass
    for c in range(column-1,column+2):
        try:
            slist.append(brd[row][c])
        except:
            pass
    for c in range(column-1,column+2):
        try:
            slist.append(brd[row-1][c])
        except:
            pass    
    return slist
