"""
na kazdej stacji :
sprawdz czy w zasiegu jest tansza stacja, jesli tak to zatankuj tylko tyle zeby do niej dojechac
jesli nie ma takiej stacji to zatankuj do pelna
"""

def petrol_cnt( stations, max_gas, destination_idx ) :

	n = len( stations )
	gas_left = 0
	idx = 0
	cnt = 0
	i = 0
	cost = 0
	curr_price = -1

	while idx + gas_left < destination_idx :

		res_idx = -1

		while i < n and stations[i][0] <= idx + gas_left :
			res_idx = stations[i][0]
			i += 1
			curr_price = stations[i][1]
		if res_idx == -1 :
			return -1

		idx = res_idx
		cnt += 1
		j = i

		while j < n and stations[ j ][ 0 ] <= idx + max_gas :
			if curr_price > stations[j][1] :
				cost += ( stations[j][0] - idx ) * curr_price
				idx = j
				i = j + 1
				cnt += 1
				break

	return cnt , cost

stations = [(0, 5), (4, 2), (7, 3), (10, 4)]
L = 6
D = 13
print( petrol_cnt( stations , L , D ) )