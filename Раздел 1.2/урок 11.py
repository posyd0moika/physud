import random
#дз
#1) Попросите пользователя ввести количество элементов для списка.
#2) Создайте список, состоящий из целых случайных чисел от 0 до 100, заданного пользователем количества.
#3) Выведите этот список с помощью цикла while.
#4) С помощью множеств удалите из списка все повторяющиеся значения.
#5) Выведите получившийся список с помощью цикла for.

x=input("Введите кол жл для списка")

spis=[int(random.random()*100) for i in range(0,int(x))]

i=0
while i<len(spis):
    print(spis[i])
    i=i+1
print("---------------")
mn=set(spis)
for s in mn:
    print(s)

print(len(mn), len(spis))






exit()
import random
x=set()
print(x)
x1=()
print(x1)

x=set("helloy")
print(x)

m=[int(random.random()*10) for i in range(5,20)]
print(m)
print("---random---")
print(int(random.random()*10))


x=list(set(range(5,10)))
print(x)