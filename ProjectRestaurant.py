Bill=0
while True:
    num=int(input("Please enter below options to order: \n 1. Veg 2. Non Veg 3. Exit\n"))
    if num ==1: # Veg 
        while True:
            num=int(input("Please enter below options to order: \n 1.Starter 2.Main Course 3.Beverages 4.Dessert 5.Exit\n"))
            if num==1: # Starter
                while True:
                    num=int(input("Please enter below options to order: \n 1.Paneer popcorn 2.Veg manchurian 3.Exit \n"))
                    if num==1: #Paneer popcorn
                        Price=100
                        Qantity=int(input("Please enter quantity of Paneer popcorn"))
                        Bill=Bill+(Price*Qantity)
                        print("Bill is : ",Bill)
                    elif num==2:  #Veg manchurian
                        Price=70
                        Qantity=int(input("Please enter quantity of Veg manchurian"))
                        Bill=Bill+(Price*Qantity)
                        print("Bill is : ",Bill)
                    elif num==3: #Exit
                        break
                    ch=input("Do you want to order starters (y/n) -> ")
                    if ch in ("y","Y"):
                        continue
                    else:
                        break 
            elif num==2: #Main Course
                while True:
                    num=int(input("Please enter below options to order: \n 1.Butter Roti 2.Paneer Masala 3.Exit \n"))
                    if num==1: #Butter Roti
                        Price=30
                        Qantity=int(input("Please enter quantity of Butter Roti"))
                        Bill=Bill+(Price*Qantity)
                        print("Bill is : ",Bill)
                    elif num==2: #Paneer Masala
                        Price=120
                        Qantity=int(input("Please enter quantity of Paneer Masala"))
                        Bill=Bill+(Price*Qantity)
                        print("Bill is : ",Bill)
                    elif num==3: #Exit
                        break
                    ch=input("Do you want to order main course (y/n) -> ")
                    if ch in ("y","Y"):
                        continue
                    else:
                        break
            elif num==3:
                while True:
                    num=int(input("Please enter below options to order: \n 1.Lassi 2.Cold drink 3.Exit \n"))
                    if num==1: #Lassi
                        Price=50
                        Qantity=int(input("Please enter quantity of Lassi"))
                        Bill=Bill+(Price*Qantity)
                        print("Bill is : ",Bill)
                    elif num==2: #Cold drink
                        Price=40
                        Qantity=int(input("Please enter quantity of Cold drink"))
                        Bill=Bill+(Price*Qantity)
                        print("Bill is : ",Bill)
                    elif num==3: #Exit
                        break
                    ch=input("Do you want to order beverages (y/n) -> ")
                    if ch in ("y","Y"):
                        continue
                    else:
                        break
            elif num==4: #Dessert
                while True:
                    num=int(input("Please enter below options to order: \n 1.Ice-cream 2.Faluda 3.Exit \n"))
                    if num==1: #ice-cream
                        Price=50
                        Qantity=int(input("Please enter quantity of Ice-cream"))
                        Bill=Bill+(Price*Qantity)
                        print("Bill is : ",Bill)
                    elif num==2: #Faluda
                        Price=80
                        Qantity=int(input("Please enter quantity of Faluda"))
                        Bill=Bill+(Price*Qantity)
                        print("Bill is : ",Bill)
                    elif num==3: #Exit
                        break
                    ch=input("Do you want to order Dessert (y/n) -> ")
                    if ch in ("y","Y"):
                        continue
                    else:
                        break
            elif num==5: #Exit of veg courses 
                break
            ch=input("Do you want to order starter, main course, beverages or dessert (y/n) -> ")
            if ch in ("y","Y"):
                continue
            else:
                break 
#**********************************************************Non-Veg***********************
    elif num ==2:
        while True:
            num=int(input("Please enter below options to order: \n 1.Starter 2.Main Course 3.Beverages 4.Dessert 5.Exit\n"))
            if num==1: # Starter
                while True:
                    num=int(input("Please enter below options to order: \n 1.Chiken popcorn 2.Chiken manchurian 3.Exit \n"))
                    if num==1: #Chiken popcorn
                        Price=120
                        Qantity=int(input("Please enter quantity of Chiken popcorn"))
                        Bill=Bill+(Price*Qantity)
                        print("Bill is : ",Bill)
                    elif num==2:  #Chiken manchurian
                        Price=100
                        Qantity=int(input("Please enter quantity of Chiken manchurian"))
                        Bill=Bill+(Price*Qantity)
                        print("Bill is : ",Bill)
                    elif num==3: #Exit
                        break
                    ch=input("Do you want to order starters (y/n) -> ")
                    if ch in ("y","Y"):
                        continue
                    else:
                        break 
            elif num==2: #Main Course
                while True:
                    num=int(input("Please enter below options to order: \n 1.Butter Roti 2.Chiken Masala 3.Exit \n"))
                    if num==1: #Butter Roti
                        Price=30
                        Qantity=int(input("Please enter quantity of Butter Roti"))
                        Bill=Bill+(Price*Qantity)
                        print("Bill is : ",Bill)
                    elif num==2: #Chiken Masala
                        Price=140
                        Qantity=int(input("Please enter quantity of Chiken Masala"))
                        Bill=Bill+(Price*Qantity)
                        print("Bill is : ",Bill)
                    elif num==3: #Exit
                        break
                    ch=input("Do you want to order main course (y/n) -> ")
                    if ch in ("y","Y"):
                        continue
                    else:
                        break
            elif num==3:
                while True:
                    num=int(input("Please enter below options to order: \n 1.Mocktail 2.Cold drink 3.Exit \n"))
                    if num==1: #Mocktail
                        Price=100
                        Qantity=int(input("Please enter quantity of Mocktail"))
                        Bill=Bill+(Price*Qantity)
                        print("Bill is : ",Bill)
                    elif num==2: #Cold drink
                        Price=40
                        Qantity=int(input("Please enter quantity of Cold drink"))
                        Bill=Bill+(Price*Qantity)
                        print("Bill is : ",Bill)
                    elif num==3: #Exit
                        break
                    ch=input("Do you want to order beverages (y/n) -> ")
                    if ch in ("y","Y"):
                        continue
                    else:
                        break
            elif num==4: #Dessert
                while True:
                    num=int(input("Please enter below options to order: \n 1.Ice-cream 2.Faluda 3.Exit \n"))
                    if num==1: #ice-cream
                        Price=50
                        Qantity=int(input("Please enter quantity of Ice-cream"))
                        Bill=Bill+(Price*Qantity)
                        print("Bill is : ",Bill)
                    elif num==2: #Faluda
                        Price=80
                        Qantity=int(input("Please enter quantity of Faluda"))
                        Bill=Bill+(Price*Qantity)
                        print("Bill is : ",Bill)
                    elif num==3: #Exit
                        break
                    ch=input("Do you want to order Dessert (y/n) -> ")
                    if ch in ("y","Y"):
                        continue
                    else:
                        break
            elif num==5: #Exit of veg courses 
                break
            ch=input("Do you want to order starter, main course, beverages or dessert (y/n) -> ")
            if ch in ("y","Y"):
                continue
            else:
                break
    elif num ==3: #Exit of veg or non veg
        break
    ch=input("Do you want to order veg or non-veg (y/n) -> ")
    if ch in ("y","Y"):
        continue
    else:
        break 
    
print("Your bill is -> ",Bill)
GST=Bill*(18/100)
print("GST -> ",GST)
Bill=Bill+GST
print("Your final bill is (adding GST)-> ",Bill)