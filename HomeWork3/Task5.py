#Задайте число. Составьте список чисел Фибоначчи, в том числе для отрицательных индексов.
#Пример:
#- для k = 8 список будет выглядеть так: [-21 ,13, -8, 5, −3, 2, −1, 1, 0, 1, 1, 2, 3, 5, 8, 13, 21]
k=int(input())
Spisok=[]
Spisok2=[]
Spisok3=[-1,0,1]
fib1=0
fib2=1
i=0
while i<k-1:
    FibSum=fib1+fib2
    fib1=fib2
    fib2=FibSum
    i+=1
    Spisok.append(fib2)
for x in Spisok:
    Spisok2.append(-x)
Spisok2.reverse()

Spisok2=Spisok2+Spisok3+Spisok
print(Spisok2)