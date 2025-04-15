def check_win_2d(board, player):
    # Check rows
    for row in board:
        if all(cell == player for cell in row):
            return True
    # Check columns
    for col in range(3):
        if all(board[row][col] == player for row in range(3)):
            return True
    # Check diagonals
    if (board[0][0] == board[1][1] == board[2][2] == player) or \
       (board[0][2] == board[1][1] == board[2][0] == player):
        return True
    return False

def check_draw( Board ) :
	for i in range( 3 ) :
		for j in range( 3 ) :
			if Board[i][j] == 0 :
				return False
	return True

def minimax( Board , symbol ) :
	# kolko-1 | X-2
	if check_win_2d(Board , 1 ) : return 1 , None
	if check_win_2d( Board , 2 ) : return -1 , None
	if check_draw( Board ) : return 0 , None

	iteration =( None, None )
	if symbol == 1 : # dla kolka
		best = -1
		for i in range( 3 ) :
			for j in range( 3 ) :
				if Board[i][j] == 0 :
					Board[i][j] = symbol
					score , _ = minimax( Board , 2 )
					Board[i][j] = 0
					if score > best :
						best = score
						if best == 1 :
							return best , (i,j)
						iteration = (i,j)

		return  best , iteration
	if symbol == 2 : # dla kolka
		best = 3
		for i in range( 3 ) :
			for j in range( 3 ) :
				if Board[i][j] == 0 :
					Board[i][j] = symbol
					score , _ = minimax( Board , 1 )
					Board[i][j] = 0
					if score < best :
						best = score
						if best == -1 :
							return best , (i,j)
						iteration = (i,j)
		return  best , iteration


B = [ [ 2, 0, 1 ],
      [ 0, 2, 1 ],
      [ 2, 0, 0 ] ]
print( minimax( B, 1) )
print( B )





