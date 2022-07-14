#Реализуйте алгоритм перемешивания списка.
from random import randint
import random
F=int(input())
def FillArray(Len):
    spisok=[]
    for x in range(0,Len):
        spisok.append(randint(1,100))

    return spisok

Spisok=(FillArray(F))
print(Spisok)
random.shuffle(Spisok)
print(Spisok)