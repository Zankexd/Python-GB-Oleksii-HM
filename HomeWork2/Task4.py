#   Задайте список из N элементов, заполненных числами из промежутка [-N, N]. Найдите произведение элементов на указанных позициях. Позиции хранятся в файле file.txt в одной строке одно число.
# Не знаю сделана ли задача правильно просто не понятно по ТЗ что от нас хотят
N=int(input())
Cell=input().split()
def FillArray(N):
    ADV=[]
    for x in range (-N,N+1):
            ADV.append(x)

    return ADV

def Stairs(spisok=[],Cell=None):
    Sum=1
    for x in Cell:
        Sum = 1
        if spisok[int(x)]>0:
            for k in range (1,spisok[int(x)+1]):
                Sum=Sum*k
        elif spisok[int(x)]<0:
            for k in range(spisok[int(x)], 0):
                Sum = Sum * k
        print(Sum)




spisok=FillArray(N)
Stairs(spisok,Cell)
print(spisok)
