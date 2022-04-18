#####HomeWork#####

#1) Узнайте, какое исключение появляется при делении числа на 0.
#2) Попросите пользователя ввести 2 числа.
#3) Выведите результат деления.
#4) Перехватите исключение при делении на 0 и выведите пользователю в качестве результата слово «бесконечность».

a=float(input("Первое число"))
b=float(input("Второе число"))
try:
    a/b
except ZeroDivisionError:
    print("Иди уроки учи")
else:
    print(a/b)









exit()
try:
    a=float("abc")
except ValueError:
    print("Невозможно")


while True:
    a=input("Введите число")
    try:
        a = float(a)
        if a<0:
            raise Exception("Число не положительное")
    except ValueError:
        print("Невозможно")
    except Exception as ex:
        print(ex)
    else:
        print("Спасибо за корректный ввод")
    finally:
        print("Завершаем програму")
        exit()