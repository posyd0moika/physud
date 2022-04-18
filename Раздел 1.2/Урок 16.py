
#import math as m
#import random
from math import sin, cos
from random import *
import math,cmath as cm
from  calc import *
#print(random.randint(0,7))
#print(m.sin(1))
###########homework###########
list1=[5,3,2,1,10]
print(bmin(list1))
print(bmax(list1))
print(bsum(list1))







exit()
###########homework###########
print(randint(4,10))
print(sin(1))

print(math.ceil(10.1))
print(cm.log10(1000))
print(div(5,10))

while True:
    com=input("Введите команду:1-сложение,2-вычитание,3-умножение,4-деление,0-выход из программы ")
    if com=="0":
        exit()
    a=float(input("Введите число первое"))
    b=float(input("Введите число второе"))
    if com=="1":
        print(sum(a,b))

    elif com == "2":
        print(sub(a, b))

    elif com == "3":
        print(mult(a, b))

    elif com == "4":
        print(div(a, b))
    else:
        print("Ты что клавиатурой не научился пользоватся")
        exit()
