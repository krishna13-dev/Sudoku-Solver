board = [[0, 4, 9, 0, 0, 0, 0, 0, 5],
		 [0, 0, 0, 8, 3, 1, 0, 0, 0],
		 [0, 0, 0, 0, 0, 0, 0, 0, 8],
		 [0, 0, 0, 0, 9, 0, 8, 1, 0],
		 [0, 0, 0, 0, 0, 7, 6, 0, 0],
		 [0, 0, 1, 0, 0, 0, 3, 0, 0],
		 [7, 8, 0, 4, 1, 0, 0, 0, 9],
		 [2, 9, 4, 7, 0, 0, 0, 0, 0],
		 [6, 0, 0, 9, 0, 0, 0, 0, 0]]

# solve board
def solve_board(board):
	find = find_empty(board)
	if not find:
		return True
	else:
		row, col = find

	for i in range(1, 10):
		if check_valid(board, i, (row, col)):
			board[row][col] = i

			if solve_board(board):
				return True

			board[row][col] = 0

	return False

# check if valid
def check_valid(board, num, pos):
	# row
	for i in range(len(board[0])):
		if board[pos[0]][i] == num and pos[1] != i:
			return False

	# coloum
	for i in range(len(board[0])):
		if board[i][pos[1]] == num and pos[0] != i:
			return False

	# 3*3 box
	box_x = pos[1] // 3
	box_y = pos[0] // 3

	for i in range(box_y*3, box_y*3 + 3):
		for j in range(box_x*3, box_x*3 + 3):
			if board[i][j] == num and (i,j) != pos:
				return False

	return True

# find empty space
def find_empty(board):
	for i in range(len(board)):
		for j in range(len(board)):
			if board[i][j] == 0:
				return(i, j)
	return None

# printing board
def print_board(board):
	for i in range(len(board)):
		if i % 3 == 0 and i != 0:
			print('- - - - - - - - - - - -')

		for j in range(len(board[i])):
			if j % 3 == 0 and j != 0:
				print(' | ', end = '')

			if j == 8:
				print(board[i][j])
			else:
				print(str(board[i][j]) + ' ', end= '')


print_board(board)
solve_board(board)
print()
print('Solved :')
print_board(board)