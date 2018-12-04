#!/usr/bin/env python3

from collections import defaultdict

def solve():
	field_claims = defaultdict(set)

	for line in open('input.txt', 'r'):
		claim_id, _, coords, rect = line.strip().split(' ')
		left, top = map(int, coords[:-1].split(','))
		width, height = map(int, rect.split('x'))

		for x in range(left, left+width):
			for y in range(top, top+height):
				field_claims[x, y].add(claim_id)

	# chop up claims to figure out which one isn't shared
	dirty_claims = set()

	for claim_set in sorted(field_claims.values(), key=len, reverse=True):
		if len(claim_set) > 1:
			dirty_claims |= claim_set
		elif dirty_claims.isdisjoint(claim_set):
			return claim_set.pop()

value = solve()

print("Untouched Claim: {}".format(value))
