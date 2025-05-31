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


def check_win( board, player ) :
	# Check rows
	for i in range( 3 ) :
		for j in range( 3 ) :
			if board[i][j] != player :
				break
		else :
			return True
	# Check columns
	for i in range( 3 ) :
		for j in range( 3 ) :
			if board[j][i] != player :
				break
		else :
			return True

	# Check diagonals
	if (board[ 0 ][ 0 ] == board[ 1 ][ 1 ] == board[ 2 ][ 2 ] == player) or (
			board[ 0 ][ 2 ] == board[ 1 ][ 1 ] == board[ 2 ][ 0 ] == player) :
		return True
	return False

def check_draw( Board ) :
	for i in range( 3 ) :
		for j in range( 3 ) :
			if Board[i][j] == 0 :
				return False
	return True

def minimax( Board , symbol ) :

	circle_ = 1
	cross_ = 2
	empty_ = 0

	if check_win_2d(Board , 1 ) : return 1 , None
	if check_win_2d( Board , 2 ) : return -1 , None
	if check_draw( Board ) : return 0 , None

	best_pair = ( None, None )
	if symbol == circle_ : # dla kolka
		best = -1
		for i in range( 3 ) :
			for j in range( 3 ) :
				if Board[i][j] == empty_ :
					Board[i][j] = symbol
					score , _ = minimax( Board , cross_ )
					Board[i][j] = 0
					if score > best :
						best = score
						if best == 1 :
							return best , (i,j)
						best_pair = (i, j)
		return  best , best_pair

	if symbol == cross_ :
		best = 3
		for i in range( 3 ) :
			for j in range( 3 ) :
				if Board[i][j] == empty_ :
					Board[i][j] = symbol
					score , _ = minimax( Board , 1 )
					Board[i][j] = 0
					if score < best :
						best = score
						if best == -1 :
							return best , (i,j)
						best_pair = (i, j)
		return  best , best_pair


B = [ [ 2, 0, 1 ],
      [ 0, 2, 1 ],
      [ 2, 0, 0 ] ]
print( minimax( B, 1) )
print( B )





