String=input("Enter the string to check -> ")
Cnt=0
for i in range(0, len(String)):  
    #print(String[i],String[len(String)-i-1])
    if String[i] != String[len(String)-i-1]: 
        Cnt=Cnt+0
    else:
        Cnt=Cnt+1
        
if (Cnt==0):
    print("{} this string is not palindrom")
else:
    print("{} this string is a palindrom")
