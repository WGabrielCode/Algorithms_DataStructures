def is_prob(t, i, j):
    # Sprawdzenie, czy istnieje inne pole, które można by zaszachować
    leng = len(t)
    for x in range(leng):
        for y in range(leng):
            if x != i and y != j and t[x][y]:
                return True
    return False


def move(t):
    leng = len(t)
    t_w = [False for _ in range(leng)]  # Wiersze już szachowane przez wieżę
    t_k = [False for _ in range(leng)]  # Kolumny już szachowane przez wieżę

    # Oznaczamy wiersze i kolumny zaszachowane przez obecne wieże
    for i in range(leng):
        for j in range(leng):
            if t[i][j]:
                t_w[i] = True
                t_k[j] = True

    # Szukamy wiersza i kolumny, które nie są szachowane
    free_rows = [i for i in range(leng) if not t_w[i]]
    free_cols = [j for j in range(leng) if not t_k[j]]

    if len(free_rows) != 1 or len(free_cols) != 1:
        # Więcej niż jedna niezajęta linia: błąd w założeniu zadania
        return None

    # Przypisujemy wiersz i kolumnę, na które powinna trafić wieża
    target_row = free_rows[0]
    target_col = free_cols[0]

    # Teraz trzeba znaleźć pozycję wieży, której przeniesienie spowodowało problem
    # Będziemy szukać wieży, która może "zakłócać" ten układ
    for i in range(leng):
        for j in range(leng):
            if t[i][j]:  # Jeśli jest wieża
                # Zmieniamy pozycję tej wieży na target_row, target_col
                t_copy = [row[:] for row in t]
                t_copy[i][j] = False
                t_copy[target_row][target_col] = True

                # Sprawdzamy, czy nowa pozycja naprawia problem
                t_w_new = [False for _ in range(leng)]
                t_k_new = [False for _ in range(leng)]

                # Nowe szachowanie wierszy i kolumn
                for x in range(leng):
                    for y in range(leng):
                        if t_copy[x][y]:
                            t_w_new[x] = True
                            t_k_new[y] = True

                # Sprawdzamy, czy wszystko zostało zaszachowane
                if all(t_w_new) and all(t_k_new):
                    return (i, j, target_row, target_col)

    return None

print()