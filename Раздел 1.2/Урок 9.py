#Домашнее задание

sp=[4,2,5,8,5,3,54,776,15,34,56]
i=0
while i<len(sp):
    print(i,'ЭЛЕМЕНТА','-',sp[i])
    i=i+1
i=0
x=input('Какой индекс вы хотите посмотреть')
while i!=int(x):
    i=1+i
if i<=len(sp):
    print("вот элеемент который вы искали", '-', sp[i])

else :
    print("Такого элемента нет")













exit()
list=["h",'e','l','l','o']

print(list[1])
print('полследний элемент',list[-1])
print('количество эл',len(list))

print('--------------------')

i=0
while i<len(list):
    print(list[i])
    i=i+1

print('--------------------')


list=['a',3,1.4,True]
i=0
while i<len(list):
    print(list[i])
    i=i+1
print('--------------------')
list[3]=False
print(list[3])



print("-----------")
list=[[1,25],[4,5,3],[2]]
print(list[1][2])
i=0
print('-----------')
while i<len(list):
    j=0
    while j<len(list[i]):
        print(list[i][j])
        j=j+1
    i=i+1

print('------------')
prices=[20,10,15,65,312,15,3]
min = prices[0]
max = prices[0]

i=1
while i<len(prices):
    if prices[i]<min:
        min=prices[i]
    if prices[i]>max:
        max=prices[i]
    i=i+1
print(max)
print(min)