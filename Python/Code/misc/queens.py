




def NonAttackingQueen(n=8):
	
	def printBoard(board, maxRow):
		for i in range(maxRow):
			print " "
			for j in range(maxRow):
				print board[i][j],
		print " "		

	def canPlaceQueen(board, row, column, maxRow):
		for i in range(0, maxRow):
			if i !=column and  board[row][i] == 'Q':
				return False

			if i!=row and  board[i][column] == 'Q':
				return False

		i = row +1 
		j = column + 1 
		while i < maxRow and j < maxRow:
			if board[i][j] == 'Q':
				return False
			i += 1
			j += 1
		
		i = row - 1
		j = column + 1
		while i >= 0 and j < maxRow:
			if board[i][j] == 'Q':
				return False
			i -= 1
			j += 1

		i = row + 1
		j = column - 1  
		while j >= 0 and i < maxRow:
			if board[i][j] == 'Q':
				return False
			i += 1
			j -= 1
		
		i = row - 1
		j = column - 1 
		while j >= 0 and i >= 0:
			if board[i][j] == 'Q':
				return False
			j -= 1
			i -= 1		

		return True


	def placeQueen(board, row, maxRow):
		
		totalPlacements = 0
		for column in range(maxRow):
			if canPlaceQueen(board, row, column, maxRow):
				board[row][column] = 'Q'
				if row == (maxRow-1):
					printBoard(board, maxRow)
					totalPlacements += 1
				else:
					newP =placeQueen(board, row+1, maxRow)
					totalPlacements += newP

			#Undo last placement
			board[row][column] = '.'			
		
		return totalPlacements


	board = [['.' for i in range(n)] for j in range(n)]

	totalPlacements = 0
	for i in range(n): #0th column
		#Place queeen on ith column
		board[0][i] = 'Q'
		t = placeQueen(board, 1,n)
		totalPlacements += t

		board[0][i] = '.'

	return totalPlacements	



print NonAttackingQueen(8)