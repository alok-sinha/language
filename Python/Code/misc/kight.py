
# - - - - -
#. - K - K -
#  K - - - K 
#. - - K - - 
#. K - - - K
#  - K - K -

def knightsTour(board,i,j, moveNo):

	def getNextPlaces(i,j):
		moves = [(i+1,j+2), (i+1, j-2), (i+2, j+1), (i+2, j-1), (i-1, j-2), (i-1, j+2),(i-2,j-1) ,  (i-2,j+1)]
		validMovees = []
		for move in moves:
			if move[0] >= 0 and move[0] <= 7 and move[1] >= 0 and move[1] <=7:
				if board[move[0]][move[1]] == 0:
					validMovees.append(move) 
		return validMovees


	nextPlaces = getNextPlaces(i,j)
	for place in nextPlaces:
		x,y = place[0], place[1]
		#print x,y, ":", moveNo
		board[x][y] = moveNo
		if moveNo == 64:
			for line in board:
				print line
			print "done"
			return 0

		d = knightsTour(board, x,y, moveNo+1)
		if d == 0:
			return 0
		else:
			board[x][y] = 0	

	return -1

board = [[0]*8 for i in range(8)]

board[0][0] = 1
knightsTour(board, 2,3,2)