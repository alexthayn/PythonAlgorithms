# Extended Euclidean Algorithm

def gcdExtended(x,y):
    if y == 0:
        return (x,1,0)
    else:
        (d,a,b) = gcdExtended(y,x%y)
        return (d,b,a-x//y*b)
print(gcdExtended(35,15))
