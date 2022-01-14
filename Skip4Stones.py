# Illustration for a(4) = 38 from Arnauld Chevallier: (retrieved from https://oeis.org/A337663)
#  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .
#
#  . 35 18 36  . 23  . 21  . 32  .  .  .  .  .
#
#  .  . 17  1  . 14  9  . 12 20  .  .  .  .  .
#
#  .  . 34 16 15  .  5  4  8  .  . 26 27  .  .
#
#  .  .  .  . 31  . 10  1  3 19 25  .  1 28  .
#
#  .  .  .  .  .  . 11  .  2  6  . 33  . 29  .
#
#  .  .  .  .  .  . 24 13 22  1  7  .  .  .  .
#
#  .  .  .  .  .  . 37  .  . 30 38  .  .  .  .
#
#  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .
#
#	y is 9
#	x is 15
#	the 1s are at (y,x): (2,3), (4,7), (4,12), (6,9)

board = []
for num1 in range(9):	
	board.append([])
	for num2 in range(15):
		board[num1].append([0,0])

def updateSums(y, x, newValue):
	for yVal in range(y-1, y+2):
		for xVal in range(x-1, x+2):
			board[yVal][xVal][1] += newValue

board[2][3][0] = 1
updateSums(2,3,1)
board[4][7][0] = 1
updateSums(4,7,1)
board[4][12][0] = 1
updateSums(4,12,1)
board[6][9][0] = 1
updateSums(6,9,1)

def printPretty():
	for rowPrint in board:
		printList = []
		for column in rowPrint:
			if column[0] < 10:
				printList.append('0' + str(column[0]))
			else:
				printList.append(str(column[0]))
		print printList

#printPretty()

def tryToPlaceRecursive(value): #we're going to try iterating only through the "mdiddle" squares, so no first or last row or column
	for y,row in enumerate(board[1:-1], 1): #this skips the first and last elements and we start the enumerate at 1 to get the right coordinates
		for x,column in enumerate(row[1:-1], 1):
			if column[1] == value and column[0] == 0:
				board[y][x][0] = value
				updateSums(y, x, value)
				tryToPlaceRecursive(value + 1)		#we go in after we place a number
				board[y][x][0] = 0
				updateSums(y, x, -value)
	if value >= 39:
		print '--- max number was ' + str(value - 1) +  ' ---'
		printPretty()

tryToPlaceRecursive(2) #this was also very fast, since the starting position was very restricted
#we confirm the given solution!