

#дз
#1) Создайте функцию, которая проверяет чётное число передано в параметре или нет. Она должна возвращать True или False.
#2) Создайте функцию, которая принимает список и возвращает максимальное значение из списка.
#3) Создайте функцию с переменным числом аргументов, внутри которой должно выводиться среднее арифметическое переданных чисел.
#Примечание: среднее арифметическое чисел равно сумме этих чисел поделённое на их количество.
import  random
def arf(nambers):
    u=0
    for c in nambers:
        u +=c
    u=u/len(list1)
    return u


list1=[100,0]
print(arf((list1)))

def chet(x): #1
    if x%2==0:
        return True
    else:
        return False
print(chet(7))

def bmax(arr):   #2
    max = arr[0]
    for k in arr:
        if k > max:
           max = k
    return max

print(bmax([5,123,5,6,756,4,]))









exit()
def printphyton():
    print("phyton")


def sum(x,y):
    return x+y
def sub(x,y):
    return x-y

def summaprint(x,y,r=False):
    s=sum(x,y)
    if r:
        return
    else:
        print(s)

def bignambers(*nambers):
    a=0
    for n in nambers:
        a +=n
    return a
def bigdict(**dict):
    for k in dict:
        print(k,"=",dict[k])


printphyton()
g=sub(10,5)
s=sum(5,7)
print(s)
print(g)

summaprint(10,7,True)

print(bignambers(4,2,3,4,6,1))

print(bigdict(name="alex",age=15))

print("-------")

l=lambda x,y:print(x+y)
l(5,7)
print((lambda x,y:(x+y)) (5,7))