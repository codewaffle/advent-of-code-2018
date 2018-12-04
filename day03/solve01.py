#!/usr/bin/env python3

def solve():
	field = set()
	result = set()

	for line in open('input.txt', 'r'):
		_, _, coords, rect = line.strip().split(' ')
		left, top = map(int, coords[:-1].split(','))
		width, height = map(int, rect.split('x'))

		claim = {(x, y)
		for x in range(left, left+width)
		for y in range(top, top+height)}

		result |= claim & field
		field |= claim

	return len(result)

value = solve()

print("Overlapping Pairs: {}".format(value))
