#Дз
#1) Создайте список из 5 чисел.
#2) Определите сумму чисел в списке и выведите её.
#3) Определите среднее арифметическое чисел в списке и выведите его.
#Примечание: при выполнении заданий используйте цикл for.

x=[1,34,2.4,10,41]
y=0
for n in x:
    y=n+y
print(y)
print(y/int(len(x)))






exit()
list1=[1, 5, 0, -4, 2.5]
for n in list1:
    print(n)
print("---------------")
str="phyton"
print(str[0])

for x in str:
    print(x)
print("-------")
for s in str:
    if s=="Y":
        break
else:
    print("Символа Y в",str,"нет")

print("-------")

list1= list(range(2, 15))
for n in list1:
    print(n)
print("-------")
x=[i for i in range(1,10)]
print(x)
print("-------")
x=[i*2 for i in range(1,10)]
print(x)

x=[i for i in range(1,10) if i%2 ==0]
print(x)