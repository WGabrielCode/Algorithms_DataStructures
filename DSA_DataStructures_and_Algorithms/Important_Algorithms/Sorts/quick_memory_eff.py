def quick_sort(T):

    def partition(T, left, right, pivot):
        i = left -1
        for j in range(left, right):
            if T[j] <= T[right]:
                i += 1
                T[i], T[j] = T[j], T[i]
        T[i+1], T[right] = T[right], T[i+1]
        return i+1

    def in_quick(T, left, right):
        while left < right:
            pivot = T[right]
            q = partition(T, left, right, pivot)

            if q - left < right - q:
                in_quick(T, left, q-1)
                left = q + 1
            else:
                in_quick(T, q+1, right)
                right = q -1

    in_quick(T, 0, len(T)-1)

def quick_sort_h(T):

    def partition(T, left, right):
        i = left
        j = right
        p_val = T[(left + right) // 2]

        while True:
            while T[i] < p_val:
                i += 1
            while T[j] > p_val:
                j -= 1
            if i >= j:
                return j
            T[i], T[j] = T[j], T[i]
            i += 1
            j -= 1

    def in_quick(T, left, right):
        while left < right:
            q = partition(T, left, right)

            if q - left < right - q:
                in_quick(T, left, q)
                left = q + 1
            else:
                in_quick(T, q+1, right)
                right = q

    in_quick(T, 0, len(T)-1)

T = [6,9,2,6,3,9,1,4,-2,-123,100]
print(T)
quick_sort(T)
print(T)

T = [6, 2, 1, 8, 3, 6, 6, 8, 4, 2, 3]
print(T)
quick_sort_h(T)
print(T)