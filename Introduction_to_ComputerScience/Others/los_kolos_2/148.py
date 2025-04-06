def main() :
    def is_safe(i, j):
        nonlocal board
        for x in range(j):
            if board[i][x]:
                return False
        x , y = i-1 , j-1
        while x >= 0 and j >= 0:
            if board[x][y]:
                return False
            x -= 1
            y -= 1

        x , y = i +1 ,j -1
        while x < 8 and j <8 :
            if board[x][y]:
                return False
            x += 1
            y -= 1
        return True
    #end def is_safe

    def solve( col ) :
        nonlocal board , num

        if col == 8 :
            num +=1
            return

        for i in range( 8 ) :
            if is_safe( i , col ) :
                board[i][col] = True
                solve(col+1)
                board[i][col] = False
    num = 0
    board = [ [ False for i in range(8)] for i in range(8) ]
    solve( 0 )
    return num
#end def main
print( main() )