#Create a module robot which has a variable name and 3 functions talk and walk. 
#Call these functions and print the variables from another file using the concept of modules. 

import RobotFunction as R1

def main():
    name=R1.Rname()
    R1.talk(name)
    R1.walk(name)

if __name__=='__main__':
    main()

