def selection_sort(t):
    for i in range(len(t)):
        minV = t[i]
        ind = i
        for j in range(i+1, len(t)):
            if t[j] < minV:
                minV = t[j]
                ind = j
        t[ind] = t[i]
        t[i] = minV
    print(t)
#end def

T = [8,3,1,5,8,4,2,1,5,83,-123,46,3,1,64,45,45,45,45,45,1,0,-2]
selection_sort(T)