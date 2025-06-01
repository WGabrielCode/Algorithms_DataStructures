# mamy liscie
# p =[3,0,2] pozywienie( dlugosc mozliwego skoku
# k = [ 1,4,1] koszt skoku z tego liscia
# f( i,e ) - liczba skokow zeby dostac sie od i-tego liscia posiadajac energie e.

# celem zadania jest znalezc min skokow do ostatniego liscia
e = 5
p = [3,0,2]
k = [1,4,1]
f = [[0 for _ in range(e+1)] for _ in range(len(p))]

for i in range(len(p)):
	for e in range(e+1):
		if i == 0:

			