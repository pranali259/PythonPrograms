#Write a menu driven program for calculator using functions for
#sum,sub,mul,div using while true loop

def Sum(a,b):
    print("Sum of numbers is: ",a+b)
def Subtraction(a,b):
    print("Subtraction of numbers is: ",a-b)
def Multiplication(a,b):
    print("Multiplication of numbers is: ",a*b)
def Division(a,b):
    print("Division of numbers is: ",a/b)

def main():
    while True:
        print("1. Addition   2. Subtraction  3. Multiplication   4.Division 5. Exit")
        Choice=int(input("Please enter operation choice which you want to perform -> "))
        if Choice==5:
            break
        num1=int(input("Please enter number 1 -> "))
        num2=int(input("Please enter number 2 -> "))
        if Choice==1:
            Sum(num1,num2)
        if Choice==2:
            Subtraction(num1,num2)
        if Choice==3:
            Multiplication(num1,num2)
        if Choice==4:
            Division(num1,num2)
        if Choice==5:
            break
        ch=input("Do you want to continue (y/n) -> ")
        if ch in ('y','Y'):
            continue
        else:
            print("Operations are done... !")
            break
if __name__=='__main__':
    main()