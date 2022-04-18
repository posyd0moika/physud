def sum(x,y):
    return x+y

def sub(x,y):
    return x-y

def mult(x,y):
    return x*y

def div(x,y):
    return x/y

def bmax(nambers):   #2
    max = nambers[0]
    for k in nambers:
        if k > max:
           max = k
    return max

def bmin(nambers):   #2
    min = nambers[0]
    for k in nambers:
        if k < min:
           min = k
    return min

def bsum(nambers):
    k=0
    x=0
    while k<len(nambers):
        x=nambers[k]+x
        k=1+k
    return x





