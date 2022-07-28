#Задайте натуральное число N. Напишите программу, которая составит список простых множителей числа N.
def Natural(n):
    Spisok = []
    d = 2
    while d * d<= n:
        if n % d==0:
            Spisok.append(d)
            n //= d
        else:
            d+= 1
    if n >1:
        Spisok.append(n)
    return Spisok
print(Natural(23141))