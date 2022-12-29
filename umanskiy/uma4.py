#Найти сумму квадратов целых чисел в составном типе из N произвольных элементов. 
#Организовать выбор режима работы: для всех чисел, только четных, только нечетных. 
#Величину N задать с клавиатуры. Произвольный составной тип создать программно с 
#помощью цикла. Начальный вид составного типа и результат его обработки вывести на 
#экран

import random
a=int(input("ВВедите размерность"))
my_list=[]
sum=0
sum_chet=0
sum_nechet=0
for i in range(a):
    x=random.randint(0,50)
    my_list.insert(i,x)
print(my_list)
print("Выберете режим работы : 1 - cумма всех чисел ; 2 - сумма только четных; 3 - сумма только нечетных ")
mode=int(input())

if mode==1:
    for i in range(len(my_list)):
        sum+=my_list[i]**2
    print ('Сумма квадратов всех элементов = ',sum)
if mode==2:
    for i in range(len(my_list)):
        if my_list[i]%2==0:
            sum_chet+=my_list[i]**2
    print ('Сумма квадратов всех четных элементов = ',sum_chet)
if mode==3:
    for i in range(len(my_list)):
        if my_list[i]%2==1:
            sum_nechet+=my_list[i]**2
    print ('Сумма квадратов всех четных элементов = ',sum_nechet)