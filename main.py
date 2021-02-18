from queen import Queen


board_set =[]
row = col = board_size = 4 
set_num = next_col_x = y_row = x_col = 0
break_loop = False

def check_cell(y, x, board_l):
	q = Queen(y, x, board_size).all_possible_move()
	for a_set in q:
		if a_set in board_l:
			return False
	return True

def pop_last_set(board):
	y, x = board.pop()
	return y, x+1

while True:
	if y_row < row and x_col < col:
		for y in range(y_row, row):
			for x in range(x_col, col):
				if check_cell(y, x, board_set):					
					board_set.append((y, x))
					y_row, x_col = y, x
					break # breaak X range
				elif x == col-1 and not check_cell(y, x, board_set):
					y_row, x_col = pop_last_set(board_set)					
					break_loop = True
					break # break X range			
			if break_loop:
				break_loop = False
				break # break Y range
			x_col = 0 # reset the start of the loop by zero

		if len(board_set) == board_size:
			set_num += 1
			print(f'ok set {set_num} = {board_set}')
			# continue search by remove the last cell set, and continue with the next cell
			y_row, x_col = pop_last_set(board_set)

	elif board_set:
		y_row, x_col = pop_last_set(board_set)
	elif not board_set:
		break # break the while loop
