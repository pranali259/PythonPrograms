def main():
    
    NumberOfT = int(input("Please enter the number of test cases between 1 to 10: "))

    for i in range(NumberOfT):
        TCase=input("Please enter the test case consists of a string : ")
        CountList=[]
        TList=[]
        CounterMax=0
        mylist=[]
        for k in TCase:
            mylist.append(k)
        print(mylist)
        mylist = list(dict.fromkeys(mylist))
        print(mylist)
        for j in mylist:
            counter1 = TCase.count(j)
            if counter1>=CounterMax:
                CounterMax=counter1
                CountList.append(CounterMax)
                TList.append(j)
             
        print("Maximum no of types count is:",CounterMax)        
        print(CountList)
        print(len(TList))
        print(TList)
        CheckList=list(dict.fromkeys(CountList))
        print(CheckList)
        #if len(TList)>1:
         #   print("In '{}' test case type '{}' people will be safe".format(TCase,TList[-1]))
        if len(TList)==1:
            print("In '{}' test case type '{}' people will be safe".format(TCase,TList[0]))
        elif len(CheckList)==1:
            CountLess=0
            FinalList=[]
            for EachChar in range(len(TList)):
                AsciiVal=ord(TList[EachChar])
                print("The ASCII value of {} char is {} : ".format(TList[EachChar],ord(TList[EachChar])))
                FinalList.append(AsciiVal)
            #print(FinalList)
            FinalList.sort()
            #print("Sorted final list : ",FinalList)
            #print("Less ASCII value is : ",FinalList[0])
            #print("This value is converted into character : ",chr(FinalList[0]))
            print("In '{}' test case type '{}' people will be safe".format(TCase,chr(FinalList[0])))
        else:
            print("In '{}' test case type '{}' people will be safe".format(TCase,TList[-1]))
if __name__=='__main__':
    main()
