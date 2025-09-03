# dp solution #nlogn

def wyprawy (WI):

    WI.sort( key = lambda x : x[1] )
    n = len( WI )
    dp = [0] * n

    print( WI )
    for i in range( n ) :

        start , finish , val = WI[i]

        if i > 0 :
            dp[i] = max( dp[i] , dp[i-1] )

        prev_idx = -1
        left = 0
        right = i - 1

        while left <= right :
            mid = (left+right) // 2

            if WI[mid][1] <= start :
                prev_idx = mid
                left = mid + 1
            else :
                right = mid - 1

        res = dp[prev_idx] if prev_idx != -1 else 0
        dp[i] = max( dp[i] , res , val + res )
    return dp[n-1]

WI = [(1, 5, 100), (3, 4, 70), (2, 4, 90), (4, 7, 60),[10,12,20]]
print( wyprawy( WI ) )

"""
line = input()
data = list(map(int, line.strip().split()))
n = len(data) // 3
WI = [None] * n
for i in range(n):
    WI[i] = (data[i*3], data[i*3+1], data[i*3+2])
print(wyprawy(WI))
"""