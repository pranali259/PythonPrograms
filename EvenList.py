Li=[-1,14,23,0,2,-9,19,-8,3]
Even=[]
Result=0
i=1
while i in Li:
    if i%2==0:
        print("{} is even.".format(i))
        Even.append(i)
        Result=Result+i
    i=i+1
print("Even list is - {} ".format(Even))
print("Sum of number is : {}".format(Result))
