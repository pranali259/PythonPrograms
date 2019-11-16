import math
x=int(input("Please enter number -> "))
y=int(input("Please enter power you want to calculate -> "))
print("Factorial of {} is {}".format(x,math.factorial(x)))
print("Exponential of {} is {}".format(x,math.exp(x)))
print("Square root of {} is {}".format(x,math.sqrt(x)))
print("{} power of {} is {}".format(y,x,math.pow(x,y)))
print("Ceiling of {} is {}".format(x,math.ceil(x)))