#Задайте список из вещественных чисел. Напишите программу, которая найдёт разницу между максимальным и минимальным значением дробной части элементов.
#Пример:
#- [1.1, 1.2, 3.1, 5, 10.01] => 0.19
k=[1,0.1,-1.3,123,-1]
def Razor(Spisok=[]):
    min=0
    max=0
    for x in Spisok:
        if min>x:
            min=x
        if max<x:
            max=x
    print(max-min)
Razor(k)