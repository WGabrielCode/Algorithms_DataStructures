# recurrent solution #nlogn (runtime error)

def wyprawy (WI):

    WI.sort()
    memo = {}
    idx_memo = {}

    def binSearch( x ) :
        if x in idx_memo :
            return idx_memo[ x ]

        left = 0
        right = len( WI )-1

        res = right + 1

        while left <= right :
            mid = (left + right) // 2

            if WI[mid][0] >= x :
                res = mid
                right = mid - 1
            else :
                left = mid + 1

        idx_memo[x] = res
        return res

    def rec( idx ) :

        if idx in memo :
            return memo[idx]

        if idx >= len( WI ):
            return 0

        res = max( rec( idx + 1 ) , WI[idx][2] + rec( binSearch( WI[idx][1] ) ) )

        memo[idx] = res
        return res


    return rec( 0 )

line = input()
data = list(map(int, line.strip().split()))
n = len(data) // 3
WI = [None] * n
for i in range(n):
    WI[i] = (data[i*3], data[i*3+1], data[i*3+2])
print(wyprawy(WI))