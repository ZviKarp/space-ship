import random 
def gen_rock(brd,height,width):#returns a random location (as long as the location is empty)
	x = random.randint(1,width-2)
	y = random.randint(0,height-5)
	if brd[y][x] == " ":
		return [x,y]
	else:
		return gen_rock(brd,height,width)
def rock_gen(brd,height,width):#returns a random location from the top of the map for a rock to come in 
	y = 0
	x = random.randint(1,width-2)
	if brd[y][x] == " ":
		return [x,y]
	else:
		return rock_gen(brd,height,width)
def move_rocks(brd,height,width):
	nlist = range(height)
	nlist.reverse()
	for r in nlist:
		for c in range(width):
			if brd[r][c] == 'O':
				if safe_move_rock(brd,r,c,height):
					pass
				else:
					return False
	return True
def safe_move_rock(brd,r,c,height):
	brd[r][c] = ' '
	if r == height-1:
		try:
			if brd[0][c] == '|':
				pass
			elif brd[0][c] == 'O':
				pass
			elif brd[0][c] == ' ':
				brd[0][c] = 'O'
			else:#hit the spaceship
				return False
			return True
		except:
			pass
	else:
		try:
			if brd[r+1][c] == '|':
				pass
			elif brd[r+1][c] == 'O':
				pass
			elif brd[r+1][c] == ' ':
				brd[r+1][c] = 'O'
			else:#hit the spaceship
				return False
			return True
		except:
			pass
	return True


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