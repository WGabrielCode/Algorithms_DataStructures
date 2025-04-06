def insertion_sort( t ) :
    for i in range( 1, len( t ) ) :
        for j in range( i-1, -1, -1 ) :
            if t[j] > t[j+1] :
                t[j],t[j+1]=t[j+1],t[j]
            else:
                break

    print(t,end='')
    print("insertion")

#end def sort

def swapping_insertion_sort(t):
    for i in range(1, len(t)):
        curNum = t[i]
        for j in range(i - 1, -1, -1):
            if t[j] > curNum:
                t[j + 1] = t[j]
            else:
                break
        t[j+1] = curNum

    print(t,end='')
    print("swap select")
#chuj

def selection_sort( t ) :
    for i in range( len(t )-1 ) :
        ind = i
        for j in range( i+1, len(t) ) :
            if t[j] < t[ind] :
                ind = j
        if ind != i :
            t[ind],t[i] = t[i] , t[ind]

    print(t, end='')
    print("select")
#end def

def bb_sort( t) :
    for i in range(len(t) -1) :
        for j in range( len(t)-1-i):
            if t[j]>t[j+1]:
                t[j],t[j+1] = t[j+1],t[j]

    print(t, end='')
    print("bbsort")

def merge_sort( t ) :

    def merge( t , low , mid , high ) :

        a = t[ low : mid + 1 ]
        b = t[ mid + 1 : high + 1 ]
        a.append( float("inf") )
        b.append( float("inf") )

        i = j = 0

        for k in range( low , high + 1 ) :
            if a[i] <= b[j] :
                t[k] = a[i]
                i += 1
            else :
                t[k] = b[j]
                j += 1
        #end def

    def merge_sort2( t , low , high ):
        if low != high :
            mid = ( low + high ) // 2

            merge_sort2( t, low , mid )
            merge_sort2( t , mid + 1 , high )
            merge( t , low , mid , high )
    #end def

    merge_sort2( t , 0 , len( t ) -1 )
    print( t ,end = "merge_sort")
    print()
#end def

    T = [8,3,1,5,8,4,2,1,5,83,-123,46,3,1,64,45,45,45,45,45,1,0,-2]
print( T.copy )
merge_sort(T.copy)
insertion_sort(T.copy)
swapping_insertion_sort(T.copy)
selection_sort(T.copy)
bb_sort(T.copy)

























