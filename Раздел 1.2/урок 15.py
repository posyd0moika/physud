#homework
p=3.141592
def rad(R):
    ra=p*R*R
    return ra
print(rad(2))

exit()
istr=True

def sum(x,y):
    s=float(x)+float(y)
    if istr:
        print(s)
    else:
        return s
def sub(x,y):
    global res
    res= float(x) - float(y)
res=0
x=input("введите первое")
y=input("введите второе")
sub(x,y)
print("разность = ",res)

print("сумма =",sum(x,y))
