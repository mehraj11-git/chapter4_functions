def greater(a,b):
    if a>b:
        return a
    return b
def greatest(a,b,c):
    if a>b and a>c:
        return a
    elif b>a and b>c:
        return b
    return c    
def greatest(a,b,c) :
    
    return greater(greater(a,b),c)
print(greatest(40,20,30))