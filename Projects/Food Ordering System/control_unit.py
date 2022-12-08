
import admin as ad
from user import user
from random import randint

crawler = True

while crawler:
    print(" Main Menu ")
    print(" 1.LOGIN AS ADMIN ")
    print(" 2.REGISTER AS USER ")
    print(" 0.TO EXIT ")
    option = int(input(" Choose the option Accordingly "))

    if option == 1:
        userName = input(" Enter the Admin Username ")
        password = input(" Enter the Admin Password ")
        if(ad.ad_content["user_name"] == userName and ad.ad_content["password"] == password):
            print(" You are Logged-in Successfully!!! ")
        
            admin_runner = True
        
            while admin_runner:
                print(" 1.ADD FOOD ITEM TO THE MENU ")
                print(" 2.EDIT THE MENU ")
                print(" 3.REMOVE AN FOOD ITEM FROM MENU ")
                print(" 4.TO VIEW THE MENU ")
                print(" 0.TO EXIT ADMIN PORTAL ")
                admin_action = int(input(" Enter the Option Accordingly "))
            
                if(admin_action == 1):
                    food = input(" Enter your Dish Name ")
                    Id = randint(100,999)   
                    quantity = int(input(" Enter your Quantity (in grams) "))
                    price = float(input(" Enter the Price (in rupees) "))
                    discount = float(input(" Enter the discount (in percentage)"))
                    stock = int(input(" Enter the Stock of the Dish ")) 
                    ad.add_menuItem(food,Id,quantity,price,discount,stock)
                    #ad.add_menuItem("burger",200,120,2,400)
                    #ad.add_menuItem("Chiken",400,700,4,79)
                    #ad.add_menuItem("ramen",500,1200,7,64)

                elif(admin_action ==2):
                    ad.edit_menuItem()
                
                elif(admin_action == 3):
                    ad.remove_menuItem()
                
                elif(admin_action == 4):
                    ad.print_menu()
                
                elif(admin_action == 0):
                    print(" You're Successfully Logged-out ")
                    admin_runner = False
                else:
                    print(" Enter a Valid Option ")
        else:
            print(" Entered Credentials are Wrong ")

                
    elif option == 2:
        U = user()
        fullName = input(" Enter the User's FullName ")
        phoneNo = input(" Enter the Phone Number ")
        Email = input(" Enter the E-mail ")
        address = input( " Enter the Address ")
        Password = input( " Enter the Password ")
        if(U.user_Registration(fullName,phoneNo,Email,address,Password) == True):
            print(" You are Registered Successfully!!! ")
        else:
            print(" Registration Unsuccessful ")
            print( " Enter  Valid Credentials ")
        
        user_runner = True
        while user_runner:
            print(" USER LOGIN MENU ")
            print(" 1.USER LOGIN ")
            print(" 0.To Exit ")
            user_action = int(input(" Choose the Option Accordingly "))

            if(user_action == 1):
                Email = input(" Enter the Registerd E-mail ")
                passcode = input( " Enter the Password ")
                if(U.user_login(Email,passcode) == True):
                    print(" User Logged-in Successfully ")

                    user_options_driver = True

                    while user_options_driver:
                        print(" USER OPTIONS MENU ")
                        print(" 1.PLACE ORDER ")
                        print(" 2.VIEW ORDER HISTORY ")
                        print(" 3.UPDATE PROFILE ")
                        print(" 0.TO EXIT ")
                        ch = int(input(" Choose Your Option Accordingly "))

                        if(ch == 1):
                            U.place_order()
                        elif (ch == 2):
                            U.order_history() 
                        elif(ch == 3):
                            U.update_profile()
                        elif(ch == 0):
                            print(" User Options Menu Logged-out Successfully ")
                            user_options_driver = False
                        else:
                            print(" Choose Valid Option (USER OPTIONS MENU)")
                else:
                    print(" User Log-in Unsuccessful ")                        
            elif(user_action == 0):
                print(" User Login Menu Logged-out Successfully ")
                user_runner = False
            else:
                print(" Choosa valid Option (USER LOGIN MENU)")            
    elif option == 0: 
        print(" You're Successfully Logged-out ")           
        crawler = False
    else:
        print(" Choose a Valid Option (main menu driver)")                    



