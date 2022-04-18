#1) Выведите число, округлив его до 2 знаков после запятой.
#2) Выведите с шагом в 1 градус все значения синуса угла от 0 до 180 градусов в таком виде: «sin(УГОЛ_В_ГРАДУСАХ) = РЕЗУЛЬТАТ».
#Примечание: разумеется, стоит использовать цикл.
from math import *
a=4.58
print(round(a,2))

i=0
while i<=180:
    print("sin(",i,")","=",sin(radians(i)),sep="")
    i=i+1

exit()



print(e)
print(pi)

print("-----")

print(sin(1))
print(cos(1))
print(tan(1))
print(1/tan(1))
print("-----")
print(sin(radians(30)))

print(degrees(1))
print("-----")
print(fabs(-5))
print(floor(5.9))
print(ceil(5.1))
print(sqrt(9))
print("-----")

print(round(4.337,3))
