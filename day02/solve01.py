#!/usr/bin/env python3
from collections import defaultdict

doubles = 0
triples = 0

for line in open('input.txt', 'r'):
	acc = defaultdict(int)

	for char in line.strip():
		acc[char] += 1

	result = set(acc.values())

	if 2 in result:
		doubles += 1

	if 3 in result:
		triples += 1

print("Doubles: {}  Triples: {}".format(doubles, triples))
print("Checksum: {}".format(doubles*triples))