"""
Dany jest ciąg zer i jedynek zapisany w tablicy T[N]. Proszę napisać funkcję, która odpo-
wiada na pytanie czy jest możliwe pocięcie ciągu na kawałki z których każdy reprezentuje liczbę pierwszą.
Długość każdego z kawałków nie może przekraczać 30. Na przykład dla ciągu 111011 jest to możliwe, a dla
ciągu 110100 nie jest możliwe.
"""
def is_prime(x):
    if x < 2:
        return False
    if x == 2 or x == 3 or x == 5:
        return True
    if x % 2 == 0 or x % 3 == 0 or x % 5 == 0:
        return False
    i = 5
    while i * i <= x:
        if x % i == 0 or x % (i + 2) == 0:
            return False
        i += 6
    return True


def main(t, p=0, current_num=0, length=0):
    if p == len(t):
        return is_prime(current_num) and length <= 30

    new_num = current_num * 2 + (1 if t[p] == '1' else 0)
    new_length = length + 1

    if new_length > 30:
        return False

    option1 = False
    if is_prime(current_num):
        option1 = main(t, p + 1, int(t[p] == '1'), 1)

    option2 = main(t, p + 1, new_num, new_length)

    return option1 or option2


T = "111011"
print(main(T))
