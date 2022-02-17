# https://www.codewars.com/kata/51fda2d95d6efda45e00004e/train/python
# DONE: create the User class
# it must support rank, progress, and the inc_progress(rank) method

class User:
	rank = 0
	progress = 0

	ranks = [x for x in range(-8, 9)]
	ranks.remove(0)

	pMax = 100
	rMax = 8

	pRankDown = 1
	pRankSame = 3

	def __init__(self):
		self.rank = -8
		self.progress = 0

	def inc_progress(self, ranked):
		if ranked < -8 or ranked > 8 or ranked == 0:
			raise ValueError('ValueError')
		pairs = [self.ranks.index(self.rank), self.ranks.index(ranked)]
		difference = abs(pairs[1] - pairs[0])
		if pairs[0] > pairs[1]:
			if difference == 1:
				self.progress += self.pRankDown
		elif difference == 0:
			self.progress += self.pRankSame
		elif difference > 0:
			self.progress += 10 * difference ** 2
		self.eval_progress()

	def eval_progress(self):
		if self.rank == self.rMax:
			self.progress = 0
			return
		while self.progress >= self.pMax:
			if self.rank >= self.rMax:
				self.progress = 0
				return
			self.progress -= 100
			self.rank += 1
			if self.rank == 0:
				self.rank = 1
			if self.rank == self.rMax:
				self.progress = 0
