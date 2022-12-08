import json
import admin as adm

class user:
    def __init__(self):
        self.User = {}
        
    def reg_validation(self,name,phone,Email,address,password):
        if(len(phone)==10 and"@" in Email and len(password)>=8 and len(name)*len(phone)*len(Email)*len(address)*len(password) != 0):
            return True
        else:
            return False  
        
    def user_Registration(self,fullName,phoneNo,Email,address,Password):
        
        
        if (self.reg_validation(fullName,phoneNo,Email,address,Password) == True):
            self.User = {"FullName":fullName, "PhoneNumber":phoneNo, "Email":Email, "Address":address,"Password":Password}
            #print(" Registration Successful!!! ")  
            return True
        else:      
            #print(" Registration unsuccessful!!! ")
            return False
            
    def user_login(self,Email,password):
        if(self.User["Email"] == Email and self.User["Password"] == password):
            #print(" Login Successful ")
            return True
        else:
            #print(" Login Unsuccessful ")
            return False
    
    def place_order(self):
        print(" Choose your orders here ")
        print(adm.print_menu())
        choice = int(input(" Do yo wish to order? 1.YES 2.NO "))
        if choice == 1:
            
                i = input("Enter the FoodId to Place Order ")
                orderId_list = []
                try:
                    orderId_list = i.split(",")
                except:
                    print(" Enter valid format ")
                else:
                    pass    
                finally:    
                    print("Your Selected Order List ", orderId_list)

                k=0
                #self.d={}
                for j in orderId_list:
                    #Food_Id = input(" Enter the Food ID to Place the Order ")
                    i = int(j)
                    Food_name = adm.Menu[i]["Food"]
                    quantity = int(input(f" Enter the {Food_name} Quantity(in Units) "))
                   
            
                    # Total Bill Amount Calculation
                    Bill_amount  = quantity*adm.Menu[i]["Price"]
            
                    # Updating the Stock (Admin)
                    stock = adm.Menu[i]["Stock"]-quantity
                    adm.Menu[i]["Stock"] = stock
                
                    # Calculating discounted bill
                    dis = self.discount(Bill_amount,adm.Menu[i]["Discount"])
                    dis_amount = Bill_amount - dis
            
                   
                    k=k+1
                    #d[k] = {"FoodName":Food_name,"Quantity":quantity,"Bill":dis_amount}
                    #d = {"FoodName":Food_name,"Quantity":quantity,"Bill":dis_amount}
                    
                    self.order_details(k,Food_name,quantity,dis_amount)

                print(" Your Current Orders: ")
                self.view_orderList()
                #print(d)

                print(" 1.TO PLACE THE ORDER ")
                print(" 0.DECLINE THE ORDER ")
                user_choice = int(input(" Choose the Option Accordingly "))

                M = 0
                self.placed_orders = {}
                print(" Your Order History: ")
                if(user_choice == 1):
                    for i,j in self.d.items():
                        M=M+1
                        self.placed_orders[M] = j
                    f = open('PlacedOrders.json',"w")
                    json.dump(self.d,f)
                    f.close()

                    self.order_history()
                    
                    print(" Your Order Placed Successfully!!! ")
                    print(" Visit again ")

                elif(user_choice == 0):
                    print(" Your Order is Cancelled ")
                else:
                    print(" Enter a Valid Option ")
                    
        elif choice == 2:
            print(" Dear Customer, you didn't place any Orders  ")
        else:
            print(" Enter a valid code ")     
    
    
    def order_details(self,k,fname,qty,bill):
        self.d[k] =  {"FoodName":fname,"Quantity":qty,"Bill":bill}

    def view_orderList(self):
        n=0
        for i in self.d:  
            n=n+1  
            print(f"{n}.{self.d[i]['FoodName']} ({self.d[i]['Quantity']}) [{self.d[i]['Bill']} INR]")

    def order_history(self):
        f = open('PlacedOrders.json', 'r+')
        content = json.load(f)
        for i in range(len(content)):
            print(content[i])
        f.close()    


        # m=0
        # for i in self.placed_orders:
        #     m=m+1
        #     print(f"{m}.{self.placed_orders[i]['FoodName']} ({self.placed_orders[i]['Quantity']}) [{self.placed_orders[i]['Bill']} INR]")
  
        
    def discount(self,bill,discount):
        discount_amount = (discount/100)*bill
        return discount_amount
        
    def update_profile(self):  
        if(len(self.User) == 0):
            print(" Kindly Register with us to Update Profile ")
        else:
            profile_driver = True
            while profile_driver:
                print(" PROFILE EDIT MENU ")
                print(" 1.EDIT WHOLE PROFILE ")
                print(" 2.EDIT A PARTICULAR FIELD ")
                print(" 0.TO EXIT UPDATE PROFILE ")
                c=int(input(" Choose Option Accordingly "))
                if(c == 1):
                    self.User["FullName"] = input(" Enter the New Name ")
                    self.User["PhoneNumber"] = input(" Enter the New PhoneNo")
                    self.User["Email"] = input(" Enter the New Email ")
                    self.User["Address"] = input(" Enter the New Address ")
                    self.User["Password"] = input(" Enter the New Password ")
                    print(" New Profile ")
                    print(self.User)
                elif(c == 2):
                    print(" 1. Edit Name")
                    print(" 2. Edit Phone Number")
                    print(" 3. Edit Email")
                    print(" 4. Edit Address")
                    print(" 5. Edit Password")
                    m = int(input(" Press the Number to Edit the Corresponding Field "))
                    
                    if(m == 1):
                        self.User["FullName"] = input(" Enter the New Name ")
                        print(" User Name Updated Successfully")
                        
                    elif(m == 2):
                        self.User["PhoneNumber"] = input(" Enter the New PhoneNo")
                        print(" Phone Number Updated Succesfully")
                        
                    elif(m == 3):
                        self.User["Email"] = input(" Enter the New Email ")
                        print(" Email Updated Successfully")
                        
                    elif(m == 4):
                        self.User["Address"] = input(" Enter the New Address ")
                        print(" Address Updated Successfully")

                    elif(m == 5):
                        self.User["Password"] = input(" Enter the New Password ")
                        print(" Password  Updated Successfully")    
                    else:
                        print(" Enter a Valid Number ")
                elif(c == 0):
                    print(" You're logged-out Successfully ")
                    profile_driver = False
