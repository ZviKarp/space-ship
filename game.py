import random 
def gen_rock(brd,height,width):#returns a random location (as long as the location is empty)
	x = random.randint(1,width-2)
	y = random.randint(0,height-5)
	if brd[y][x] == " ":
		return [x,y]
	else:
		return gen_rock(brd,height,width)
def move_lasers(brd,height,width):
	for r in range(height):
		for c in range(width):
			if brd[r][c] == "|":
				move_laser(brd,r,c)
	return 0		
def move_laser(brd,row,column):
	brd[row][column] = " "
	if row == 0:
		return 0
	try:
		if brd[row-1][column] == "O":
			brd[row-1][column] = " "
			return 0
		else:
			brd[row-1][column] = "|"
	except:
		pass
	return 0