# class Board:
# 	def __init__(self, right, left, up, down):
# 		self.right = right
# 		self.left = left
# 		self.up = up
# 		self.down = down


class Queen:
	def __init__(self, x, y):
		# super().__init__(self.right, self.left, self.up, self.down)
		self.x = x
		self.y = y
		self.max = 8
		self.min = 1


	def right(self):
		return [(r, self.y) for r in range(self.x+1, self.max+1)]

	def left(self):
		return [(l-1, self.y) for l in range(self.x, self.min, -1)]

	def hor(self):
		return self.left() + self.right()

	def up(self):
		return [(self.x, u-1) for u in range(self.y, self.min, -1)]

	def down(self):
		return [(self.x, d) for d in range(self.y+1, self.max+1)]

	def vir(self):
		return self.up() + self.down()

	def up_right(self):
		return [(self.x+ur, self.y-ur) for ur in range(1, self.max+1) if self.x+ur <= self.max and self.y-ur >= self.min]

	def dwon_right(self):
		return [(self.x+dr, self.y+dr) for dr in range(1, self.max+1) if self.x+dr <= self.max and self.y+dr <= self.max]

	def up_left(self):
		return [(self.x-ul, self.y-ul) for ul in range(1, self.max+1) if self.x-ul >= self.min and self.y-ul >= self.min]

	def down_left(self):
		return [(self.x-dl, self.y+dl) for dl in range(1, self.max+1) if self.x-dl >= self.min and self.y+dl <= self.max]

	def right_axis(self):
		return self.up_right() + self.down_left()

	def left_axis(self):
		return self.up_left() + self.dwon_right()

	def all_possible_move(self):
		return self.hor() + self.vir() + self.right_axis() + self.left_axis()


def check_queen_cell(q_sets, set_l):
	for a_set in q_sets:
		if a_set in set_l:
			return False
	return True

set_lst = []
cheked_set = []
set_num = 0
def check_loop(row, set_lst, cheked_set, inc, set_num):
	row += 1
	row_x = 1

	if row == 9:
		set_num += 1
		print(f'{set_num}- {set_lst}')
		row = 0
		check_loop(row, set_lst, cheked_set, inc, set_num)

	if row == 1:
		if inc == 0:
			inc += 1
		else:
			row_x += inc
			inc += 1

	for x in range(row_x, 9):
		if row == 1:
			set_lst = []
			cheked_set = []
			# if inc == 0:
			# 	inc += 1
			# else:
			# 	x += inc
			# 	inc += 1


		if (x, row) not in cheked_set:
			set_lst.append((x, row))
			q = Queen(x, row).all_possible_move()
			if check_queen_cell(q, set_lst):
				print(set_lst)
				check_loop(row, set_lst, cheked_set, inc, set_num)
			else:
				cheked_set.append(set_lst.pop())

check_loop(0, set_lst, cheked_set, 0, set_num)
#########################################################
#########################################################
# set_lst = []
# cheked_set = []
# def check_loop(row, set_lst, cheked_set, inc):
# 	# start_col = 1
# 	# end_col = 5
# 	row += 1
# 	# print(row)
# 	if row == 5:
# 		print(set_lst)
# 		row = 0
# 		check_loop(row, set_lst, cheked_set, inc)

# 	for x in range(1, 5):
# 		# print(f'x ={x}')
# 		if row == 1:
# 			set_lst = []
# 			cheked_set = []
# 			inc += 1
# 			x += inc

# 		if (x, row) not in cheked_set:
# 			set_lst.append((x, row))
# 			q = Queen(x, row).all_possible_move()
# 			if check_queen_cell(q, set_lst):
# 				# if row <= 4:
# 					# print(set_lst)
# 					# print(cheked_set)
# 					# row = row + 1
# 				# print (f'row= {row}')
# 				check_loop(row, set_lst, cheked_set, inc)
# 				# elif row == 5:
# 				# 	print(set_lst)
# 				# 	row = 1
# 				# 	check_loop(row, set_lst, cheked_set)
# 			else:
# 				# if row != 5:
# 				cheked_set.append(set_lst.pop())
# 				# else:
# 				# 	print('test')
# 				# 	row = 1

# check_loop(0, set_lst, cheked_set, 0)
###########################################################
###########################################################

# for row1_x in range(1, 5):
# 	set_lst = []
# 	cheked_set = []
# 	if (row1_x, 1) not in cheked_set:
# 		set_lst.append((row1_x, 1))
# 		q1 = Queen(row1_x, 1).all_possible_move()
# 		if check_queen_cell(q1, set_lst):

# 			for row2_x in range(1, 5):
# 				if (row2_x, 2) not in cheked_set:
# 					set_lst.append((row2_x, 2))
# 					q2 = Queen(row2_x, 2).all_possible_move()
# 					if check_queen_cell(q2, set_lst):

# 						for row3_x in range(1, 5):
# 							if (row3_x, 3) not in cheked_set:
# 								set_lst.append((row3_x, 3))
# 								q3 = Queen(row3_x, 3).all_possible_move()
# 								if check_queen_cell(q3, set_lst):

# 									for row4_x in range(1, 5):
# 										if (row4_x, 4) not in cheked_set:
# 											set_lst.append((row4_x, 4))
# 											q4 = Queen(row4_x, 4).all_possible_move()
# 											if check_queen_cell(q4, set_lst):
# 												print(set_lst)
# 											else:
# 												cheked_set.append(set_lst.pop())
# 												# print(cheked_set)
# 												# break
# 								else:
# 									cheked_set.append(set_lst.pop())
# 									# print(cheked_set)
# 									# break
# 					else:
# 						cheked_set.append(set_lst.pop())
# 						# print(cheked_set)
# 						# break
# 		else:
# 			cheked_set.append(set_lst.pop())
# 			# print(cheked_set)
# 			# break



# def moves(row1_x, row1_y):
# 	all_8q_move = [(row1_x, row1_y)]
# 	for y in range (2, 9):
# 		for x in range (1, 9):
# 			loop = True
# 			q = Queen(x,y).all_possible_move()
# 			for i in q:
# 				if i in all_8q_move:
# 					# print(f'x{x} y{y} {i}')
# 					# print(all_8q_move)
# 					loop = False
# 					break
# 			if loop:
# 				all_8q_move.append((x,y))
# 				# for item in q:
# 				# 	all_8q_move.append(item)

# 				print(x, y)
# 				# break
# 	print(all_8q_move)

# for x in range(1, 9):
# 	# 1 for y
# 	moves(x, 1)
# q1 = Queen(1, 1).all_possible_move()
# q2 = Queen(3, 2).all_possible_move()
# print(q1)
# print(q2)


