def quick_sort(T):

    def partition(T, l, r):
        i = l - 1
        mid = (l + r) // 2
        T[mid], T[r] = T[r], T[mid]
        pivot = T[r]
        for j in range(l, r):
            if T[j] <= pivot:
                i += 1
                T[i], T[j] = T[j], T[i]
        T[i+1], T[r] = T[r], T[i+1]
        return i+1

    def in_quick(T, left, right):
        stos = [(left, right)]
        while stos:
            l, r = stos.pop()
            if l < r:
                q = partition(T, l, r)
                stos.append((l, q-1))
                stos.append((q+1, r))

    in_quick(T, 0, len(T)-1)
    return T
