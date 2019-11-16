print("All the double digit numbers divisible by 2 and 3 simultaneously: ")
for i in range(10,99):
    if i%2==0 and i%3==0:
        print(i,end=", ")