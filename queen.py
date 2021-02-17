class Queen:
	def __init__(self, y, x):
		self.x = x
		self.y = y
		self.max = 8
		self.min = 0


	def right(self):
		return [(self.y, r) for r in range(self.x+1, self.max)]

	def left(self):
		return [(self.y, l-1) for l in range(self.x, self.min, -1)]

	def hor(self):
		return self.left() + self.right()

	def up(self):
		return [(u-1, self.x) for u in range(self.y, self.min, -1)]

	def down(self):
		return [(d, self.x) for d in range(self.y+1, self.max)]

	def vir(self):
		return self.up() + self.down()

	def up_right(self):
		return [(self.y-ur, self.x+ur) for ur in range(1, self.max) if self.x+ur < self.max and self.y-ur >= self.min]

	def dwon_right(self):
		return [(self.y+dr, self.x+dr) for dr in range(1, self.max) if self.x+dr < self.max and self.y+dr < self.max]

	def up_left(self):
		return [(self.y-ul, self.x-ul) for ul in range(1, self.max) if self.x-ul >= self.min and self.y-ul >= self.min]

	def down_left(self):
		return [(self.y+dl, self.x-dl) for dl in range(1, self.max) if self.x-dl >= self.min and self.y+dl < self.max]

	def right_axis(self):
		return self.up_right() + self.down_left()

	def left_axis(self):
		return self.up_left() + self.dwon_right()

	def all_possible_move(self):
		return [(self.y, self.x)] + self.hor() + self.vir() + self.right_axis() + self.left_axis()
