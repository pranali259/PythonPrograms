num=int(input("Enter the number -> "))
Temp=num
Sum=0
Div=num/2
i=1
while i<=Div:
    if(num%i==0):
        Sum=Sum+i
    i=i+1
print("Sum of divisors is = ",Sum)
if Temp==Sum:
    print("Number {} is perfect number.".format(num))
else:
    print("Number {} is not a perfect number.".format(num))