# https://www.codewars.com/kata/52ec24228a515e620b0005ef/train/python

def exp_sum(n):
	p = [1] + [0] * n
	for k in range(1, n + 1):
		for i, x in enumerate(range(k, n + 1)):
			p[x] += p[i]
	return p[n]


print(exp_sum(5))
