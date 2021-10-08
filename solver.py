board = [
	[5, 0, 0, 0, 7, 0, 0, 0, 0],
	[6, 0, 0, 1, 9, 5, 0, 0, 0],
	[0, 9, 8, 0, 0, 0, 0, 6, 0],
	[8, 0, 0, 0, 6, 0, 0, 0, 3],
	[4, 0, 0, 8, 0, 3, 0, 0, 1],
	[7, 0, 0, 0, 2, 0, 0, 0, 6],
	[0, 6, 0, 0, 0, 0, 2, 8, 0],
	[0, 0, 0, 4, 1, 9, 0, 0, 5],
	[0, 0, 0, 0, 8, 0, 0, 7, 9]
]


#Solving the whole thing
def auto_solve(board):

	empty = search_empty(board)  #finds an empty spot with zero

	if not empty:
		return True       #while not empty returns true  until finds an empty spot
	else:
		row , col = empty    #assigns the empty position to row and col

	for i in range(1, 10):
		if possible(board, i, (row, col)):   
			board[row][col] = i    #assigns a value from 1-10 if appropiate

			if auto_solve(board):   #starts the whole thing again to do the rests
				return True
			else:
				board[row][col] = 0
	return False


#Checking if the number is in the correct position
def possible(board, num, pos):
	for i in range(len(board[0])):
		if (board[pos[0]][i] == num and pos[1] != i) or (board[i][pos[1]] == num and pos[0] != i): #check if the selected number is
																									#is the same row or col of empty spot
			return False

	x = pos[1] // 3
	y = pos[0] // 3

	for i in range(y*3, y*3 + 3):
		for j in range(x*3, x*3 + 3):
			if board[i][j] == num and (i, j) != pos:       #checks if the number is in the same small box of 9 elements
				return False

	return True


#Finds spaces with zero and returns the positions of the empty spot
def search_empty(board):
	for i in range(len(board)):
		for j in range(len(board[0])):
			if board[i][j] == 0:
				return (i, j)


#Printing the borad
def print_b(board):
	
	for i in range(len(board)):
		if i%3 == 0 and i != 0:		#Draws a line after 3 rows
			print('-----------------------')
		
		for j in range(len(board[0])):
			if j%3 == 0 and j !=0:
				print(' | ', end='')   #Draws a line after 3 cols

			if j == len(board) - 1:
				print(board[i][j])     #Makes new line after the last element in the row
			else:
				print(f"{board[i][j]} ", end = '') 		#Prints the element spearating with space 
print_b(board)
print("---------------------------")
print("---------------------------")
auto_solve(board)
print_b(board)
