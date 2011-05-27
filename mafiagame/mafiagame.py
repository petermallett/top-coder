import random

games = [
	[3, [1, 1, 1], 1.0],
	[5, [1, 2, 3], 0.0],
	[20, [1, 2, 3, 4, 5, 6, 7, 1, 2, 3, 4, 5, 6, 7, 18, 19, 0], 0.0],
	[23, [17, 10, 3, 14, 22, 5, 11, 10, 22, 3, 14, 5, 11, 17], 0.14285714285714285]
]

def vote_lowest(players, opinions):
	if (len(players) != len(opinions)):
		nonvoter_count = len(players) - len(opinions)
		for x in range(0, nonvoter_count):
			min_votes = min(votes)
			min_count = votes.count(min_votes)
			if (min_count == 1):
				index = votes.index(min_votes)
			else:
				# choose one of the players with the min votes to vote for
				min_indexes = []
				for i, v in enumerate(votes):
					if (v == min_votes):
						min_indexes.append(i)
					if (len(min_indexes) == min_count):
						break
				index = random.randrange(0, len(min_indexes))
			
			# vote for the selected player
			votes[index] += 1

# search the current votes for a losing player
# if there is a loser, return the index
# if not return 0 and update vulnerable
def check_state(votes, vulnerable):
	max_votes = max(votes)
	if (votes.count(max_votes) == 1):
		return votes.index(max_votes)
	else:
		for i, v in enumerate(votes):
			if (v == max_votes):
				vulnerable[i] = 1
			else:
				vulnerable[i] = 0
		return 0

def play(players, opinions):
	vulnerable = []

	# first vote
	for x in opinions:
		players[x]['votes'] += 1
	# complete first vote
	vote_lowest(players, opinions)

	result = check_state(players, vulnerable)
	print(result)

def probabilityToLose(playerCount, opinions):
	# initialize players
	players = []
	for x in range(0, playerCount):
		players.append({'votes': 0, 'losses': 0})
	
	play(players, opinions)
	
for x in games:
	player_count = x[0]
	opinions = x[1]
	expected = x[2]
	prob = probabilityToLose(player_count, opinions)
	if (prob != expected):
		print('error: ', prob, ' should be ', expected)