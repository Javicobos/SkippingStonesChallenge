# Illustration for a(5) = 49: by Andrew Howroyd at https://oeis.org/A337663/a337663.txt
# +----+----+----+----+----+----+----+----+----+----+----+----+----+
# |    |    |    |    |    |    |    |    |    | 42 |    | 25 | 49 |
# +----+----+----+----+----+----+----+----+----+----+----+----+----+
# |    |    |    |    | 45 |    |    |    | 41 |    |  1 | 24 |    |
# +----+----+----+----+----+----+----+----+----+----+----+----+----+
# |    |    |    |    | 29 | 16 | 31 |    | 27 | 14 |    | 23 | 47 |
# +----+----+----+----+----+----+----+----+----+----+----+----+----+
# |    |    |    | 12 |  1 |    | 15 |    | 13 |    | 22 |    |    |
# +----+----+----+----+----+----+----+----+----+----+----+----+----+
# |    |    | 44 |    | 11 | 10 | 43 |  5 | 38 |  8 |    | 40 |    |
# +----+----+----+----+----+----+----+----+----+----+----+----+----+
# |    |    |    | 32 | 21 |    |  9 |  4 |  1 |  7 | 18 |    |    |
# +----+----+----+----+----+----+----+----+----+----+----+----+----+
# | 37 |    | 33 |    |    | 30 |    | 17 |  3 |  2 |  1 | 19 | 39 |
# +----+----+----+----+----+----+----+----+----+----+----+----+----+
# | 36 |  1 | 34 |    |    |    |    | 48 | 28 |  6 |    | 20 |    |
# +----+----+----+----+----+----+----+----+----+----+----+----+----+
# |    | 35 |    |    |    |    |    |    |    |    | 26 | 46 |    |
# +----+----+----+----+----+----+----+----+----+----+----+----+----+
#
#		9 rows so the required y is 11
#		13 cols so the required x is 15

board = []
for num1 in range(11):	
	board.append([])
	for num2 in range(15):
		board[num1].append([0,0])

def updateSums(y, x, newValue):
	for yVal in range(y-1, y+2):
		for xVal in range(x-1, x+2):
			#if board[yVal][xVal][0] == 0:
			board[yVal][xVal][1] += newValue
			#else:
			#	print 'we tried to update cell: (' + str(yVal) + ', ' + str(xVal) + ') with value ' + str(newValue)

board[2][11][0] = 1
updateSums(2,11,1)
board[4][5][0] = 1
updateSums(4,5,1)
board[6][9][0] = 1
updateSums(6,9,1)
board[7][11][0] = 1
updateSums(7,11,1)
board[8][2][0] = 1
updateSums(8,2,1)

def printPretty():
	for rowPrint in board:
		printList = []
		for column in rowPrint:
			if column[0] == 0:
				printList.append('  ') #changed to spaces here to make it more visually clear
			elif column[0] < 10:
				printList.append(' ' + str(column[0]))
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
				updateSums(y, x, -value)
				board[y][x][0] = 0					
	if value >= 50:
		print '--- max number was ' + str(value - 1) +  ' ---'
		printPretty()

tryToPlaceRecursive(2) #this found four solutions almost immediately, yay
#the last solution matches the given one! we confirm it