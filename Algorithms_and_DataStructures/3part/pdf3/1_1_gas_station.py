
def petrol_cnt( stations , gas , destination_idx ) :
	idx = 0
	n = len( stations )
	i = 0
	cnt = 0
	while idx + gas < destination_idx :
		res_idx = -1
		while i < n and stations[i] <= idx + gas :
				res_idx = stations[i]
				i += 1

		if res_idx == -1 :
			return -1
		cnt += 1
		idx = res_idx
	return cnt


stations = [ 4, 6, 7, 11, 14, 17, 21 ]
L = 4
D = 25
print( petrol_cnt( stations , L , D ) )