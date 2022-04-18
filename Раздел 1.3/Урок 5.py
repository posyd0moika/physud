#####Домашнее задание#####
import random

d={"Hello":"Привет","Bay":"Пока","Lesson":"Урок"}

def sr(x):
    while True:
        a = d.get(x)
        b = input("Переведите слово на англ-" + a + ":")
        if b.lower() == x.lower():
            print("Вы перевели правильно")
            break
        elif b.lower() == "show":
            print(d)
        elif b.lower() == "quit":
            exit()
        else:
            print("Вы ввели неправильно \nПовторите попытку\n")

while True:
    r=random.randrange(0,3) ##r=0,1,2
    if r==0:
        x = "Hello"
        sr(x)
    elif r==1:
        x = "Bay"
        sr(x)
    elif r==2:
        x = "Lesson"
        sr(x)













exit()
##############################




d={"name":"semen","age":19}
print(d)
d.setdefault("work",True)
print(d)
print(d.get("age"))

##d.pop("age")
print(d)

print(list(d.keys()))

print(list(d.values()))

d["age"]=40
d["Male"]=True
print(d)
d.clear()