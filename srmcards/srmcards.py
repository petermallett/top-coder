# http://www.topcoder.com/stat?c=problem_statement&pm=11341&rd=14429
stacks = [
	(1, [498, 499]),
	(4, [491, 492, 495, 497, 498, 499]),
	(4, [100, 200, 300, 400]),
	(6, [11, 12, 102, 13, 100, 101, 99, 9, 8, 1]),
	(4, [118, 321, 322, 119, 120, 320]),
	(7, [10, 11, 12, 13, 14, 1, 2, 3, 4, 5, 6, 7, 8, 9])
	]

def removeSingles(cards):
	turns = 0
	for x in cards:
		d1, d2 = x - 1, x + 1
		if (not d1 in cards and not d2 in cards):
			turns += 1
			cards.remove(x)
	return turns

def removeDoubles(cards):
	turns = 0
	for x in cards:
		d1, d2 = x - 1, x + 1
		if (not (d1 in cards and d2 in cards) and (d1 in cards or d2 in cards)):
			turns += 1
			cards.remove(x)
			if (d1 in cards):
				cards.remove(d1)
			else:
				cards.remove(d2)
	return turns

def maxTurns(cards):
	turns = 0
	while (len(cards) != 0):
		turns += removeSingles(cards)
		turns += removeDoubles(cards)
			
	return turns

for x in stacks:
	print(maxTurns(x[1]), ' turns, should be: ', x[0])
