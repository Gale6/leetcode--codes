def surroundedRegions(board):

	if len(board) <=2:
		return board

	oNotOnBoarder = []
	oOnBoarder = []
	directionMatrix = [[-1,0],[1,0],[0,-1],[0,1]]


	for i in range (len(board)):
		for j in range (len(board[0])):
			if board[i][j] == 'O':
				if i == 0 or i == len(board) - 1 or j == 0 or j == len(board[0]) - 1:
					oOnBoarder.append([i,j])
				else:
					oNotOnBoarder.append([i,j])
	print(oOnBoarder,'===',oNotOnBoarder)
	x = 0
	while x < len(oOnBoarder):
		for direct in directionMatrix:
			nr,nc = oOnBoarder[x][0] + direct[0], oOnBoarder[x][1] + direct[1]
			if 1 <= nr and nr < len(board) - 1 and 1 <= nc and nc < len(board[0]) - 1 and board[nr][nc] == 'O':

				if [nr,nc] in oNotOnBoarder:
					oNotOnBoarder.pop(oNotOnBoarder.index([nr,nc]))
					oOnBoarder.append([nr,nc])
		x += 1
	while len(oNotOnBoarder) != 0:
		temp = oNotOnBoarder.pop()
		board[temp[0]][temp[1]] = 'X'

	return board


board = [["X","O","X","O","X","O"],["O","X","O","X","O","X"],["X","O","X","O","X","O"],["O","X","O","X","O","X"]]
for j in board:
	print(j)
for i in (surroundedRegions(board)):
	print(i)