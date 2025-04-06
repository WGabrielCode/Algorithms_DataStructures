def King(N, L):
    t = [[0 for i in range(N)] for _ in range(N)]
    for i in L:
        x, y = i
        t[x][y] = 1

    def fun(n, t, i, j, cnt):
        if i < 0 or i >= n or j < 0 or j >= n:
            return False
        if t[i][j] == 1:
            return False
        if i == n-1 and j == n-1:
            return True

        moves = [(1,0), (0,1), (1,1)]
        for dx, dy in moves:
            if fun(n, t, i+dx, j+dy, cnt+1):
                return True
        return False

    return fun(N, t, 0, 0, 0)

