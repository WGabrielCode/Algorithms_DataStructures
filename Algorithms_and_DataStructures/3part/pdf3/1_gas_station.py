
def minRefuelStops( target , startFuel , stations ) :
	from queue import PriorityQueue

	pq = PriorityQueue()

	for idx, val in stations :
		pq.put( (-val, idx) )

	curr_idx = 0
	cnt_stations = 0
	tmp = [ ]

	while curr_idx + startFuel < target :
		if pq.empty() :
			return -1
		petrol_val, petrol_idx = pq.get()
		if curr_idx + startFuel >= petrol_idx :
			cnt_stations += 1
			startFuel = startFuel - (petrol_idx - curr_idx) - petrol_val
			curr_idx = petrol_idx
			for a in tmp :
				pq.put( a )
		else :
			tmp.append( (petrol_val, petrol_idx) )

	return cnt_stations
"""
target = 100
startFuel = 10
stations = [[10,60],[20,30],[30,30],[60,40]]

target = 1000
startFuel = 83
stations = [[22,17],[100,23],[121,71],[141,77],[236,4],[438,78],[500,76],[642,66],[672,20],[685,81]]

target = 3
startFuel = 1
stations = [[1, 1]]
"""
target = 10
startFuel = 3
stations = [ [ 2, 5 ], [ 4, 2 ] ]
#Output: 2
print( minRefuelStops( target , startFuel , stations ) )