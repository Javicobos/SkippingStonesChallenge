# data structure: array of arrays for the basic chess board
# we will use some upper bound for the board size that i'm not sure of yet
# on each cell (board position) we'll have a list consisting of:	
#	the number on the cell, 0 if empty
#	the sum of values in its vicinity
#
#	https://www.youtube.com/watch?v=m4Uth-EaTZ8&ab_channel=Numberphile
#	https://oeis.org/A337663


# board[y][x] = [1, 23]

board = []

for num1 in range(10):	#let's start wth a 10x10 board, optimal solution fits in 8x8 chess board but let's give it some extra margins idk
	board.append([])
	for num2 in range(10):
		board[num1].append([0,0])

def updateSums(y, x, newValue): #this is going to assume we always have a neighbor because I'm making the matrix large enough
	for yVal in range(y-1, y+2):
		for xVal in range(x-1, x+2):
			board[yVal][xVal][1] += newValue

board[4][4][0] = 1
updateSums(4,4,1)

board[6][6][0] = 1
updateSums(6,6,1)

#for i in range(2,20):	#20 as max number even though I know it's 16
#	for y,row in enumerate(board):
#		for x,column in enumerate(row):
#			if column[1] == i:
#				print 'number ' + str(i) + ' at ' + str(y) + ', ' + str(x)
#				board[y][x][0] = i
#				updateSums(y, x, i)
#				break						#this should probably be a function
#		else:							#if you ended naturally, keep going (go to the y loop)
#			continue
#		break							#if you ended because we broke out of the inner loop, break out of this one too
#	else:								#if you ended naturally after iterating thru everything, end the main loop because we could not place our stone
#		break

def printPretty():
	for rowPrint in board:
		printList = []
		for column in rowPrint:
			if column[0] < 10:
				printList.append('0' + str(column[0]))
			else:
				printList.append(str(column[0]))
		print printList


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
	if value == 17:
		print '------------------------------------'
		printPretty()

tryToPlaceRecursive(2)
