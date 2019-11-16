def Calc_Fact(n):
    if n==1:
        return 1
    else:
        return (n * Calc_Fact(n-1))

def main():
    num=int(input("Enter the number which you want to calcuate factorial for -> "))
    print("Factorial of number {} is {}".format(num,Calc_Fact(num)))
if __name__=='__main__':
    main()