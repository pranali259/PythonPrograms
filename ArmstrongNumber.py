num=int(input("Enter a number -> "))
Temp=num
Div=0
Power=0
while num!=0:
    Div=num%10
    #print("Div is -> {}".format(Div))
    Power=Power+(Div*Div*Div)
    #print("Power is -> {}".format(Power))
    num=num//10
if (Temp==Power):
    print("Number {} is armstrong number".format(Temp))
else:
    print("Number {} is not a armstrong number".format(Temp))