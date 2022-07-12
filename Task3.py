X=int(input("Please type number "))
Y=int(input("Please type number "))
if X==0 or Y==0:
    print("Please type not 0")
elif X>0 and Y>0:
    print("X","Y","1")
elif X<0 and Y>0:
    print("X","Y","2")
elif X<0 and Y<0:
    print("X","Y","3")
elif X>0 and Y<0:
    print("X","Y","4")