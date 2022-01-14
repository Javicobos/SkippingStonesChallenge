board = []

for num1 in range(13):	
	board.append([])
	for num2 in range(9):
		board[num1].append([0,0])  #board size from https://github.com/ladouce7/Stepping-Stones/blob/main/LadouceurFinalProject.ipynb

def updateSums(y, x, newValue): #this is going to assume we always have a neighbor because I'm making the matrix large enough
	for yVal in range(y-1, y+2):
		for xVal in range(x-1, x+2):
			board[yVal][xVal][1] += newValue

board[3][5][0] = 1
updateSums(3,5,1)

board[7][3][0] = 1
updateSums(7,3,1)

board[9][5][0] = 1
updateSums(9,5,1)


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

def tryToPlaceRecursive(value):
	for y,row in enumerate(board):
		for x,column in enumerate(row):
			if column[1] == value and column[0] == 0:
				#print 'number ' + str(value) + ' at ' + str(y) + ', ' + str(x)
				board[y][x][0] = value
				updateSums(y, x, value)
				tryToPlaceRecursive(value + 1)		#we go in after we place a number
				board[y][x][0] = 0
				updateSums(y, x, -value)
	#print 'done with ' + str(value)
	if value >= 29:
		print '--- max number was ' + str(value - 1) +  ' ---'
		printPretty()

tryToPlaceRecursive(2) #this was very fast
#with the 1s already placed, we can confirm the a(3) = 28 
#solutions seem to perfectly match the bottom five in https://github.com/ladouce7/Stepping-Stones/blob/main/LadouceurFinalProject.ipynb
