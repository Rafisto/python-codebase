# https://www.codewars.com/kata/5a045fee46d843effa000070/train/python

import math


def decomp(d):
	factors = []
	for n in range(2, d + 1):
		x = n
		while x % 2 == 0:
			factors.append(2)
			x = x / 2
		for i in range(3, int(math.sqrt(x)) + 1, 2):
			while x % i == 0:
				factors.append(i)
				x = x / i
		if x > 2:
			factors.append(int(x))
	value = ''
	for x in range(2, d + 1):
		if factors.count(x) != 0:
			if factors.count(x) == 1:
				value += str(x) + ' * '
			else:
				value += str(x) + '^' + str(factors.count(x)) + ' * '
	return value[:-3]


print(decomp(14))
