
def DriverCode( others , W0 )




W1 = [4] * 8
W2 = [10]
W3 = [10, 6]
W4 = [2.75] * 6
W5 = [4, 6, 2]
others = [W1, W2, W3, W4, W5]
W0 = [2.5, 3.5]
print( DriverCode(others, W0) ) # 3


W1 = [4] * 8
others = [W1]
W0 = [2.5, 3.5]
print( DriverCode(others, W0) ) # 4


W1 = [4] * 8
W2 = [4] * 8
W3 = [4] * 8
W4 = [4] * 8
W5 = [4] * 8
W6 = [4] * 8
others = [W1, W2, W3, W4, W5, W6]
W0 = [2.5, 3.5]
print( DriverCode(others, W0) ) # 6
