#Создать из 2-х целочисленных списков один кортеж. Размерность создаваемых списков 
#должна задаваться с клавиатуры. Списки создать программно, используя генератор.
#Вычислить сумму всех элементов, а также суммы четных и нечетных элементов 
#сформированного кортежа. Исходные списки и созданный кортеж, а также результаты 
#обработки вывести на экран.
import random
a=int(input("ВВедите размерность 1 списка "))
b=int(input("ВВедите размерность 2 списка "))
list=[]
list2=[]
sum=0
sum_chet=0
sum_nechet=0
for i in range(a):
    x=random.randint(0,50)
    list.insert(i,x)
print(list)
for i in range(b):
    x=random.randint(0,50)
    list2.insert(i,x)
print(list2)
tuple_list=list+list2
toup = tuple(tuple_list)
print(toup)

for i in range(len(toup)):
    if toup[i]%2==0:
        sum_chet+=toup[i]
    else:
        sum_nechet+=toup[i]
    sum+=toup[i]
print("сумма всех элементов = ",sum)
print("сумма четных элементов = ",sum_chet)
print("сумма нечетных элементов = ",sum_nechet)

    