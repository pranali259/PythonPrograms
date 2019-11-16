num=int(input("Enter a number -> "))
Temp=num
Div=0
Sum=0
while num!=0:
    Div=num%10
    #print("Div is -> {}".format(Div))
    Sum=Sum+Div
    #print("Power is -> {}".format(Power))
    num=num//10
print("Sum of digit of number {} is {} ".format(Temp,Sum))