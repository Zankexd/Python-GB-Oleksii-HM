#Напишите программу, которая будет преобразовывать десятичное число в двоичное.
#Пример:
#- 45 -> 101101
#- 3 -> 11
#- 2 -> 10
k=int(input())
def Doodle(k):
    while k>=1:
        print(k%2)
        k//=2
Doodle(k)