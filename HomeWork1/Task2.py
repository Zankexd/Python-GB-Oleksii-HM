for X in True,False:
    for Y in True,False:
        for Z in True,False:
            print (not (X or Y or Z) == (not X and not Y and not Z))

