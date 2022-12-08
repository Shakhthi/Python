import json
from random import randint 

#admin_credential = {"user_name":"mathan", "password":"mathan@1234"}
with open('admin_credentials.json','r+') as AdminFile:
    ad_content = json.load(AdminFile)
AdminFile.close()


Menu = {}

#welcome to Menu Creation section
def add_menuItem(food,Id,quantity,price,discount,stock):
    Id = randint(100,999)   
    Menu[Id] = {"Food":food, "Quantity":quantity, "Price":price, "Discount":discount, "Stock":stock}

    f = open('Menu.json','w+')
    json.dump(Menu[Id],f)
    f.close()
    
    # formatted item adding             
    if(len(Menu) == 1):
        print(" New Food Item Added Successfully!!! ")
    elif(len(Menu)>1):
        print(" Food Item Appended Successfully!!! ")  
    else:
        pass
    

    # for printing the dictionary in a format that i wished to see
    #print(" New Menu after Item Added")
    #print_menu()
                    
def edit_menuItem():
    #welcome to Menu Edit section
    print_menu()
    food_id = int(input(" Enter the Food ID to Edit the Food item "))
    Menu[food_id].update( Food = input("Edit the Food Name "), 
                      Quantity = input(" Edit the Quantity "), 
                      Price = float(input(" Edit the Price ")), 
                      Discount = float(input(" Edit the Discount Rate ")), 
                      Stock = input(" Edit the Stocks left "))
    
    #print(" Dish Edited successfully!!! ")
    #print(f" New Menu after Edited Item at Food ID {food_id}")
    #print_menu()
    
        
def remove_menuItem():
    print_menu()
    removal_id = int(input(" Enter Food ID to Remove a Food Item from Menu "))
    r = Menu.pop(removal_id)
    print(f" Deletion Details: Dish ID: '{removal_id}' ")
    print(" Food Item deleted successfully!!! ")
    
    #print(" New Menu after Item Deletion ")
    #print_menu()

    
def print_menu():
    if(len(Menu) == 0):
        print( "Menu is Empty ")
    else: 
        i=0   
        for ID in Menu:
            i+=1
            print(f"{i}.Food ID:{ID} Food Name:{Menu[ID]['Food']}  Quantity:{Menu[ID]['Quantity']}gms  Price:{Menu[ID]['Price']}INR  Discount:{Menu[ID]['Discount']}%  Stock:{Menu[ID]['Stock']}Units")


 




