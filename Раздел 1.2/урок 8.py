#Домашнее задание
5
x=0
print("введите команду чтобы выбрать команду\n '+' sum \n '-' razn\n '*' umnozhenie\n '/' devide \n 0 to exit")
x = int(input("введите число\n"))
while True:
    su=input()#("введите команду чтобы выбрать команду\n '+' sum \n '-' razn\n '*' umnozhenie\n '/' devide \n 0 to exit")
    if su=="+":
        a=int(input())
        print("Получилось-",a+x)
        x=a+x
    elif su=="-":
        a = int(input())
        print("Получилось-", a - x)
        x = a - x
    elif su == "*":
        a = int(input())
        print("Получилось-", a * x)
        x = a * x
    elif su == "/":
        a = int(input())
        print("Получилось-", float(a / x))
        x = a / x
    elif su == "0":
        print("Вы вышли из программы")
        break
    else:
        print("Вы ПИДОР!")
        print("Попробуй снова!")

exit()









i=0
while i<10:
    i=i+1 #i+=1
    print('helloy world')

i = 0
while i < 10:
    i = i + 1  # i+=1
    print(i)

i=0
while i<10:
    i=i+1
    if i!=5:
        print(i)

i=0
while i<10:
    i=i+1
    if i==5:
        continue
    if i==8:
        break
print(i)

a=0
x=1
to=10
while x<=to:
    a+=x
    x+=1
print('Сумма чисел от 0 до',to,'равна',a)

while True:
    code= input('Введите 0 для входа')
    if code=="0":
        break
exit(0)
i=0
while True:
    i=i+1
    print(i)
