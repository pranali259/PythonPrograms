for i in range(1,10):
    for space in range(i,40):
        print(" ",end="")
    for j in range(1,i+1):
        if j==1:
            print(" * ",end="")
        
    print("\n")   
for k in range(11,1,-1):
    for space2 in range(40,k,-1):
        print(" ",end="")
    for l in range(k,1,-1):
        print(" * ",end="")
    print("\n")
    