Bulba=[3,21,4,5,2,1]
def Count(Bulba=[]):
    count=0
    for x in range(len(Bulba)):

        if x%2==1:
            count+= 0+Bulba[x]

    print(count)
Count(Bulba)