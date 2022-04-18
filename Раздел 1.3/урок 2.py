#1) Попросите пользователя ввести произвольную строку.
#2) Выведите коды всех символов строки, введённой пользователем.
#3) Попросите пользователя ввести строку, состоящую только из цифр.
#4) Используя соответствующую функцию, проверьте введённую пользователем строку, и если он ввёл правильно, то написать «Спасибо!»,
#иначе выбросить исключение, в обработке которого вывести строку «Некорректный ввод!».

#s1=input("Введите произовльную строку:")
#for k in s1:
    #print(ord(k))

s2=input("введите строку только из цифр:")

tr=s2.isdigit()
if tr==True:
    print("Спасибо")
else:
    print("Вы ввели не првильно")











exit()

def isfloat(x):
    try:
        float(x)
        return True
    except ValueError:
        return False


s1="str1"
s2="str2"
print(len(s1))

print(s1[1])
print(s1[0:3])

s1="abc\nxyz"  #если нужно игнорировать \n то лучше поставить \\n
s2=r"abc\nxyz"
print(s1)
print(s2)

s1="helloy"
print(s1*2)
print(s1.find("l"))
print(s1.find("l",3))

print("59".isdigit())  #Проверяет является ли строка числовой
print(s1.isalpha())

print(s1.upper())
print(s1.lower())

print("-----")

print(ord("a"))
print(chr(90))

z="     helloy     "
print(z)
print(z.strip())

s1="здрайствуйте, {0} . Вам {1} лет"

print(s1.format("Semen",30))

s1="здрайствуйте, {name} . Вам {age} лет"
print(s1.format(name="Semen",age=30))
date=("semen",10)

s1="здрайствуйте, {0[0]} . Вам {0[1]} лет"
print(s1.format(date))

s1="int: {0:d}; bin: {0:b}"
print(s1.format(5))

s1="round (150/47):{0:.3}"

print(s1.format(150/47))