#Вычислить число pi c заданной точностью d Пример:
#- при $d = 0.001, π = 3.141.$    $10^{-1} ≤ d ≤10^{-10}$
import math

d=float(input())
count=0
if d<1:
    while d%1!=0:
        count+=1
        d*=10
    print(f"{math.pi:.{count}f}")
else:
    print(f"{math.pi:.{int(d)}f}")
