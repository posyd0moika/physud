#1) Попросите пользователя указать, какое количество элементов надо создать в списке.
#2) Сделайте цикл на соответствующее число итераций, в каждой из которых просите пользователя ввести число
# в таком формате: «Введите число N:», где N – текущий номер числа.
#3) Добавляйте каждое это число в список.
#4) По завершению цикла выведите получившийся список.
n=int(input("Укажите количество элекментов в списке:"))
i=0
list=[]
while i<n:
    N=input("Введите число N:")
    list.append(N)
    i=i+1
print(list)








exit()

list =[1,2,0,5]
print(list)
list.append(9)
print(list)
list.extend([0,3,1])
print(list)
list.insert(0,5)
print(list)

print("-------")
print(list.index(0,4))
print(list.count(0))
print("-------")
list.reverse()
print(list)
list.remove(0)
print(list)
list.pop(3)
print(list)
#list.clear()
#print(list)
list.sort()
print(list)
list.sort(reverse=True)
print(list)

t=tuple("Helloy")
print(t)
print(t.index("l"))
print(t.count("l"))


