
print('Домашнее задание') #Домашнее задание

x=int(input("первое число:"))
y=int(input('Второе число(Второе число не может быть "0"):'))
if y==int('0'):
    print('Так не прокатит')
else:
    print('x/y=',x/y)

    print('Введите число 0,1 или 2')
    a = input()

    if a == '0':
        print('Вы ввевели ноль')
    elif a == '1':
        print('Вы ввевели еденицу')
    elif a == '2':
        print('Вы ввевели двойку')
    else:
        print('Ввели неправильно')

    com = a == "0" or a == "1" or a == "2"
    if com:
        x = 0
    else:
        x = 3
    print('x=', x)

    x = 0 if com else 3
    print('x=', x)
