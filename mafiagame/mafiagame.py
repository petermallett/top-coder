games = [
	[3, [1, 1, 1], 1.0],
	[5, [1, 2, 3], 0.0],
	[20, [1, 2, 3, 4, 5, 6, 7, 1, 2, 3, 4, 5, 6, 7, 18, 19, 0], 0.0],
	[23, [17, 10, 3, 14, 22, 5, 11, 10, 22, 3, 14, 5, 11, 17], 0.14285714285714285]
]

def play(players, opinions):
	vulnerable = []

	# first vote
	for x in opinions:
		players[x]['votes'] += 1
	
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
		print('error')