#Задайте список из n чисел последовательности $(1+\frac 1 n)^n$ и выведите на экран их сумму.
#Пример:
#- Для n = 6: {1: 4, 2: 7, 3: 10, 4: 13, 5: 16, 6: 19}

N2=int(input())
def Regular(N2):
    adv=[]
    Sum=1
    for x in range(1,N2+1):
        Sum=Sum+3

        adv.insert(x,Sum)

    return adv



N=(Regular(N2))
print(N)