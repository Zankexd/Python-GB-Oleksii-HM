X=int(input())
Y=int(input())
Z=int(input())

print (not(X or Y or Z) == (not X and not Y and not Z))