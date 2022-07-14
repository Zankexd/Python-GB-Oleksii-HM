
#Напишите программу, которая принимает на вход вещественное число и показывает сумму его цифр.
#Пример:
#- 6782 -> 23
#- 0,56 -> 11

N=float(input())
def Sum (N):
    Sum=0
    if N>1:
        while N>0:
            Sum=N%10+Sum
            N=N//10
    if N<1:
        K=0
        for x in str(N+1):
            K=K+1
        N=N*10**K
        while N>0:

            Sum=N%10+Sum
            N=N//10

    print(Sum)


Sum(N)