#Задана натуральная степень k. Сформировать случайным образом список коэффициентов (значения от 0 до 100) многочлена и записать в файл многочлен степени k.
#Пример:
#- k=2 => 2*x² + 4*x + 5 = 0 или x² + 5 = 0 или 10*x² = 0

import math
import random
a,b,c=0,random.randint(0,100),random.randint(0,100)
k=int(input())
with open ("file.txt","w") as file:

   c= [f"{a}*x**{k}+{b}*x+{c}=0"]

for x in c:
    if x<=1:
        x=" "
print (c)
