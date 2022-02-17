# https://www.codewars.com/kata/566584e3309db1b17d000027/train/python

def differentiate(equation, point):
	print(equation)
	value = 0
	signs = list(
		map(int, list(''.join([s for s in equation if s == '-' or s == '+']).replace('-', '0').replace('+', '1'))))
	if equation[0] != '-': signs.insert(0, 1)
	powers, vals = [[], []]
	for line in list(filter(None, equation.replace('-', '+').split('+'))):
		if line[0] == 'x':
			line = '1' + line
		if '^' in line:
			vals.append(int(line.split('^')[0].replace('x', '')))
			powers.append(int(line.split('^')[1]))
		else:
			vals.append(int(line.replace('x', '')))
			powers.append(1 if ('x' in line) else 0)
	for x in range(len(signs)):
		if powers[x] != 0:
			value += (-1 if signs[x] == 0 else 1) * powers[x] * vals[x] * point ** (powers[x] - 1)
	print(signs)
	print(vals)
	print(powers)
	return value


print(differentiate("-5x^2+10x+4", 3))
