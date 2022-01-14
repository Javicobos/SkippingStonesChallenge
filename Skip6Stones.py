#Solution at https://oeis.org/A337663 from Bert Dobbelaere
#required y is 16
#required x is 19 FIXED 18

import cProfile

board = []
for num1 in range(16):	
	board.append([])
	for num2 in range(18):
		board[num1].append([0,0])

#def updateSums(y, x, newValue):
#	for yVal in range(y-1, y+2):
#		for xVal in range(x-1, x+2):
#			#if board[yVal][xVal][0] == 0:
#			board[yVal][xVal][1] += newValue

def updateSums(y, x, newValue):
	board[y-1][x-1][1] += newValue
	board[y-1][x][1] += newValue
	board[y-1][x+1][1] += newValue
	board[y][x-1][1] += newValue
#	board[yVal][x][1] += newValue #why bother updating self
	board[y][x+1][1] += newValue
	board[y+1][x-1][1] += newValue
	board[y+1][x][1] += newValue
	board[y+1][x+1][1] += newValue

board[2][15][0] = 1
updateSums(2,15,1)
board[5][12][0] = 1
updateSums(5,12,1)
board[6][9][0] = 1
updateSums(6,9,1)
board[9][6][0] = 1
updateSums(9,6,1)
board[11][4][0] = 1
updateSums(11,4,1)
board[13][7][0] = 1
updateSums(13,7,1)

#print board
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

def tryToPlaceRecursive(value): 
	for y,row in enumerate(board[1:15], 1): 
		for x,column in enumerate(row[1:17], 1):
			if column[1] == value and column[0] == 0:
				board[y][x][0] = value
				updateSums(y, x, value)
				tryToPlaceRecursive(value + 1)		#we go in after we place a number
				updateSums(y, x, -value)
				board[y][x][0] = 0
	if value >= 61:
		print '--- max number was ' + str(value - 1) +  ' ---'
		printPretty()

#tryToPlaceRecursive(2) #took about 20 seconds

cProfile.run('tryToPlaceRecursive(2)')
#try 0: 10913133 function calls (9921058 primitive calls) in 19.725 seconds
#first potential optimization: only update sums if cell to update is empty
#	adds extra checks but prevents extra work, let's see what happens
#	requires changing order of the setting to zero and updating value in main function
#try 1: 10913133 function calls (9921058 primitive calls) in 20.021 seconds
#	ths did not save time :(
#	let's try swapping the order of checks in main function
#try 2: 10913133 function calls (9921058 primitive calls) in 27.122 seconds
#	that also did not work, let's go back to the original arrangement
#try 3: 19.670 seconds
#	4.8 seconds are spent in updateSums
#	everything else in main function
#	there's 1.6s in {range} so let me change the iterator a bit (hardcode it so -1 is the actual number)
#try 4: 19.716 seconds
#	that range must be in updatesums
#	I'll try an ugly hardcoded version of updatesums
#try 5: 16.387 seconds
#	LETSGOOO
#	we no longer spend time in range, and the time in updateSums went from around 5 seconds to 1.6

#	an idea for further work: instead of transversing the whole matrix square each time, make a list of where each number can go
#	so for example we write 2, update the sums of surrounding numbers, see 3, add those coordinates to list
#	and now we'd have a list of 4 candidates for 3 tha we can choose from
#	this heavily increases updateSums time as now it has to check for values greater than what we are placing and write the coordinates in the list
#		it is also possible that we "ruin" a sum that was already written so it's not trivial to handle this and to make it fast
#		we would have to check before we add, if we find a coincidence pop those coordinates from the og sum that was there
#		then we would add the new number's coordinates to the corresponding place
#		some questions arise here about speed:
# 			do we check that a sum is in [value+1, 60] to write it? guessing we do
# 			how to handle backtracking, if we keep a single list? not super sure right now
# 			would this whole thing be worth it? i want to believe but honestly idk, will probably make an alt version of the program to check#

#lol I just saw I'm using an extra column? let's fix that by lowering max x and redcing the x of all 1s by 1
#	this can save some time