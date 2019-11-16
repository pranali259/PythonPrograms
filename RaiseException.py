#Write a exception in main block
'''
def validate(age):
    if age<=18:
        raise ValueError("not eligible for votting...!")
    else:
        print("Eligible for votting")

try:
    validate(19)
except ValueError as ve:
    print(ve)
finally:
    print("Finally block")
'''

#write a exception in function
'''
def validate(age):
    if age<=18:
        try:
            raise ValueError("not eligible for votting...!")
        except ValueError as ve:
            print(ve)
    else:
        print("Eligible for votting")

#try:
validate(19)
#except ValueError as ve:
    #print(ve)
#finally:
 #   print("Finally block")
 '''

#User define exception
# as a developer as per your software need we creates Exceptions
#Known as user define exception
# to create user define exception we have to inherit parent exception class
#name is exception

class AgeValidError(Exception):
    pass
class Votting:
    bjp=0
    AAP=0
    MNS=0
    nota=0
    def __init__(self):
        self.name=input("Enter Name -> ")
        self.age=int(input("Enter age -> "))
        self.adharno=input("Enter adhar no -> ")
    def vote(self):
        if self.age<18:
            raise AgeValidError("Invalid age for votting...!")
        else:
            print("1. BJP \n2. AAP \n3. MNS \n4.nota")
            ch=int(input("Enter your vote -> "))
            if ch==1:
                Votting.bjp=Votting.bjp+1
            elif ch==2:
                Votting.AAP+=1
            elif ch==3:
                Votting.MNS+=1
            else:
                Votting.nota+=1
def main():
    while True:
        try:
            v=Votting()
            v.vote()
        except AgeValidError as av:
            print(av)
        finally:
            print("wait for result")
        ch=input("next voter plz...(y/n) -> ")
        if ch in ('y','Y'):
            continue
        else:
            break
    print("**************Result*************")
    print("1. BJP \t2. AAP \t3. MNS \t4.nota")
    print(Votting.bjp,"\t",Votting.AAP,"\t",Votting.MNS,"\t",Votting.nota)
    













