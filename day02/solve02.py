#!/usr/bin/env python3

def solve():
	previous_vals = []

	for line in open('input.txt', 'r'):
		# calculate current value
		line_val = set(enumerate(line.strip()))

		# compare against values already seen
		for val in previous_vals:
			diff = line_val - val

			if len(diff) == 1:
				# calculate shared characters
				solved_set = line_val & val

				# sort back into position and return compiled string
				return ''.join(x[1] for x in sorted(solved_set, key=lambda pair:pair[0]))

		# store for following loops
		previous_vals.append(line_val)

value = solve()

print("Common Letters: {}".format(value))