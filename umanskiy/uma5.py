#Создать функцию, определяющую, есть ли контрольный элемент в составном типе из N
#целочисленных элементов. Произвольный целочисленный составной тип создать 
#программно с помощью генератора для диапазона 1 - 60. Ввод контрольного значения и 
#величину списка задать с клавиатуры. Вывести исходный список на экран. Определить, 
#имеется ли контрольный элемент в составном типе, и если имеется, то в каком количестве. 
#Порядковые номера найденных элементов записать в отдельный составной тип. Вывести на 
#экран результаты обработки. Если элемент не найден, вывести сообщение об этом
import random
a=int(input("ВВедите размерность "))
my_list=[]
new_list=[]

for i in range(a):
    x=random.randint(0,60)
    my_list.insert(i,x)
print(my_list)

def funсt():
    count=0
    n=int(input('ВВедите элемент который хотите найти '))
    for i in range(len(my_list)):
        if my_list[i]==n:
            count+=1
            new_list.append(i)
    if count==0:
        print("Элементы не найдены")
    else:
        print('колличество элементов в списке- ',count)
        print('список с поряжковыми номерами элементов ',new_list)
funсt()

