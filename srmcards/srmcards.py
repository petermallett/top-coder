# http://www.topcoder.com/stat?c=problem_statement&pm=11341&rd=14429
import math

stacks = [
	(1, [498, 499]),
	(4, [491, 492, 495, 497, 498, 499]),
	(4, [100, 200, 300, 400]),
	(6, [11, 12, 102, 13, 100, 101, 99, 9, 8, 1]),
	(4, [118, 321, 322, 119, 120, 320]),
	(7, [10, 11, 12, 13, 14, 1, 2, 3, 4, 5, 6, 7, 8, 9])
	]

def maxTurns(cards):
	runlen = 0
	turns = 0
	for i, v in enumerate(cards):
		prev_i = i - 1
		if (i == 0):
			runlen = 1
		elif (v == (cards[prev_i] + 1)):
			runlen += 1
		else:
			turns += int(math.ceil(runlen / 2))
			runlen = 1
	if (runlen > 0):
		turns += int(math.ceil(runlen / 2))

	return turns


for x in stacks:
	x[1].sort()
	print(maxTurns(x[1]), ' turns, should be: ', x[0])