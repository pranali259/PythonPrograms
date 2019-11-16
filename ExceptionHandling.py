'''
1. Regular try with except

'''
'''
def demo(a,b):
    l=[10,20]
    try:
        x=a/b
        print(x)
        print(l[3])
    except ZeroDivisionError as zd:
        print(zd)
    except IndexError as ie:
        print(ie)
    except Exception as e:
        print(e)
    print("Continue code...")
demo(10,1)
'''
'''
def demo(a,b):
    l=[10,20]
    try:
        try:
            x=a/b
            print(x)           
        except ZeroDivisionError as zd:
            print(zd)

        try:
            print(l[3])
        except IndexError as ie:
            print(ie)
            
    except Exception as e:
        print(e)
    print("Continue code...")
demo(10,0)
'''


