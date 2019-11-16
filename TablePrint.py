num=int(input("Please enter number which you want to print table -> "))
i=1
print("table of {} is -> ".format(num))
while i<=10:
    print("{} X {} = {}".format(num,i,num*i))
    i=i+1