import sys
import random
import datetime
print("                 WELCOME TO OUR HOTEL           ")
branch = int(input(" Press 1 for Islamabad branch\n Press 2 for Lahore branch\n Press 3 for Karachi Branch: "))
if branch== 1:
    print(" You opted for ISLAMABAD BRANCH  ")
elif branch == 2:
    print(" You opted for LAHORE BRANCH  ")
else:
    print(" You opted for KARACHI BRANCH  ")
cost=[]

def main_menu():
    print("          WELCOME TO THE MAIN MENU       ")
    choice=int(input(" Press 1 to enter Customer Details\n Press 2 for Room Selection and Rent\n Press 3 for Laundry bill\n Press 4 for Restaurant Bill\n Press 5 for Total Cost \n Press 6 to exit: "))
    if choice == 1:
            customer_details()
    if choice == 2:
            roomselection_rent()
    if choice == 3:
            laundrybill()
    if choice == 4:
            restaurantbill()
    if choice == 5:
            totalcost()
    if choice == 6:
            sys.exit(1)
            
def customer_details():
    details=[]
    weeks = ['Monady', 'Tuesday','Wednesday','Thursday','Friday','Saturday','Sunday']
    idc = False
    print( " CUSTOMER DETAILS MENU ")
    x=input("Enter your name: ")
    details.append(x)
    y=input("Enter your address: ")
    details.append(y)
    z2=input("Enter your checkin date day(DD): ")
    z1=input("Enter your checkin date month(MM): ")
    z3=input("Enter your checkin date year(YYYY): ")
    if int(z1[0] == 0):
        z1= int(z1[1])
    else:
        z1=int(z1)
    z2=int(z2)
    z3=int(z3)
    z=datetime.datetime(z3,z1,z2)
    details.append(z)
    while idc != True:
        a=input("Enter your idcard number: ")
        if len(a)<14 or len(a)>14:
            print("Invalid Id card")
        else:    
            details.append(a)
            idc= True
    print(' Name: ',details[0],'\n Id card NO: ',details[3],'\n Address : ',details[1],'\n Checkin date: ',details[2],'and day : ',weeks[z.weekday()])

def roomselection_rent():
    rent = 0
    r=[]
    print("\n ROOM SELECTION MENU ")
    option = 0
    choice = True
    summ=0
    while option != 5:
        option = int(input("Press 1 for single bed room ---- RS 2000"
                           "\npress 2 for double bed room ---- RS 3000"
                           "\npress 3 for family room -------- RS 5000"
                           "\npress 4 for suite -------------- RS 8000"
                           "\npress 5 to exit : "))
        if option == 1:
            nights = int(input("Enter the no of nights you will stay ? "))
            room_no = random.randint(1,20)
            print("You chose the single room. your room number is ",room_no)
            rent = nights * 2000
            r.append(rent)
            choice = False
            rent = 0
        if option == 2:
            nights = int(input("Enter the no of nights you will stay ? "))
            room_no = random.randint(20,50)
            print("You chose the double room. your room number is ",room_no)
            rent = nights * 3000
            r.append(rent)
            choice = False
            rent =0 
        if option == 3:
            nights = int(input("Enter the no of nights you will stay ? "))
            room_no = random.randint(50,90)
            print("You chose the family room. your room number is ",room_no)
            rent = nights * 5000
            r.append(rent)
            choice = False
            rent=0
        if option == 4:
            nights = int(input("Enter the no of nights you will stay ? "))
            room_no = random.randint(95,100)
            print("You chose the suite. your room number is ",room_no)
            rent = nights * 8000
            r.append(rent)
            choice = False
            rent=0
    if choice == True:
            print("No option selected.Thank you for using Room Selection Menu.\n")
    else:
        for i in range(len(r)):
            summ += r[i]
        print("Your room rent is ",summ)    
        cost.append(summ)
        
def laundrybill():
    print('   WELCOME TO OUR LAUNDRY MENU   ')
    lcost=[]
    choice = 0
    choicee = True
    summ = 0 
    while choice != 5:
        choice=int(input(" Press 1 for Shirts\n Press 2 for Pants\n Press 3 for DressCoats \n Press 4 for Sweaters\n Press 5 to exit: "))
        if choice == 1:
            i=int(input("How many shirts you want for Laundry: "))
            lcost.append(i*20)
            i=0
            choicee = False
        if choice == 2:
            i=int(input("How many pants you want for Laundry: "))
            lcost.append(i*15)
            i=0
            choicee = False
        if choice == 3:
            i=int(input("How many Dresscoats you want for Laundry: "))
            lcost.append(i*70)
            choicee = False
            i=0
        if choice == 4:
            i=int(input("How many sweaters you want for Laundry: "))        
            lcost.append(i*40)
            choicee = False
            i=0
    if choicee == True:
        print("No option selected.Thank you for using Landry Menu.")
    else:    
        for element in range(len(lcost)):
            summ += lcost[element]
        print("Your total laundry bill is Rs.",summ)
        cost.append(summ)

def restaurantbill():
    print("\n   WELCOME TO OUR RESTAURANT BILL MENU   ")
    food_cost = []
    option = 0
    choicee = True
    while option != 5:
        option = int(input("press 1 for water --------- RS 10"
                            "\npress 2 for breakfast ---- RS 200"
                            "\npress 3 for lunch -------- RS 250"
                            "\npress 4 for dinner ------- Rs 300"
                            "\npress 5 for exit : "))
        if option == 1:
            i = int(input("Enter the quantity = "))
            food_cost.append(i * 10)
            choicee = False
        if option == 2:
            i = int(input("Enter the quantity = "))
            food_cost.append(i * 200)
            choicee = False
        if option == 3:
            i = int(input("Enter the quantity = "))
            food_cost.append(i * 250)
            choicee = False
        if option == 4:
            i = int(input("Enter the quantity = "))
            food_cost.append(i * 300)
            choicee = False
    if choicee == True:
        print("No option selected.Thank you for using Restaurant Bill Menu.")
    else:
        summ = 0
        for i in range(len(food_cost)):
            summ += food_cost[i]
        print("Your restaurant bill is : ",summ)
        cost.append(summ)
        
def totalcost():
    print("    HOTEL BILL    ")
    summ = 0
    for i in range(len(cost)):
        summ += cost[i]
    print("Total Bill = ",summ)
    
def main():
    confirm = "y"
    while confirm =="y":
        main_menu()
        confirm = input("Press y to continue: ")
        
main()