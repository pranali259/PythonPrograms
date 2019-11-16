num=[13,15,17,22,25,18,12]
Evenlist=[]
Div5list=[]
for i in num:
    if i%2==0:
        Evenlist.append(i)
print("Even list is -> {}".format(Evenlist))
Evenlist.sort()
print("Sorted even list is -> {}".format(Evenlist))
print("Highest number from even list -> {}".format(Evenlist[-1]))

for j in num:
    if j/5==0:
       Div5list.append(j)
print("Division by 5 list is -> {}".format(Div5list))
Div5list.sort()
print("Sorted list division by 5 -> {}".format(Div5list))
print("Highest number from division by 5 list -> {}".format(Div5list[-1]))