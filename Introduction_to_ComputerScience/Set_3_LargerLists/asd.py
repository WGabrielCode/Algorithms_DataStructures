
odw= [1,3,5,7,10,24]

def waga(t,n,p=0):
    if n==0: return True
    if p==len(t): return False
    return waga (t,n-t[p], p+1) or waga (t,n,p+1)
# end def
for w in range (1,50):
    print (w, waga (odw, w))