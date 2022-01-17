import datetime
import random
from customer import Customer

atm = Customer(id) #instance object from Customer using the id parameter

while True: #start looping with the true value
    id = int(input("Enter your pin:"))
    trial = 0

    while (id != int(atm.checkPin()) and trial < 3): #looping verification using while
        id = int(input("The pin you entered is wrong, please try again:"))
        trial += 1

        if trial == 3: #if user enter the wrong pin more than 3 times, program will directly exit
            print("You have entered the wrong pin 3 times, now we block your card. please take your card and contact customer service for assistance")
            exit()

    selectMenu = 0
    while True:  #if user enter the correct pin, program will continue to menu page
        print("Welcome")
        print("\n1 - Check Balance \t 2 - Debit \t 3 - Save \t 4 - Change Pin \t 5 - Exit")

        selectMenu = int(input("\n Choose Menu:"))#enter number to select menu

        if selectMenu == 1: #if user click no 1, it will print out the newest balance
            print("\n Your Balance is now: Rp. " + str(atm.checkBalance())+"\n") #print balance by calling the check balance function

        elif selectMenu == 2: #if user click no 2, it will debit some amount of money
                nominal = float(input("Enter the nominal balance:")) #user need to input the amount of money
                checkWithdraw =input("Confirm: You will make a debit with this following nominal? " + str(nominal) + " ") #confirming transaction

                if checkWithdraw == "y": #checking balance before debiting
                    print("Your Balance is: Rp. " + str(atm.checkBalance()) + "")
                else:
                    break
                if nominal < atm.checkBalance(): #program will debit money if user fullfil the condition
                    atm.withdrawBalance(nominal)
                    print("Debit Transaction Success")
                    print("Your Balance Now is: Rp. " + str(atm.checkBalance())+"") #printing updated balance
                else: #will stop continue if debit nominal > balance
                    print("Sorry. You don't have enough balance to continue this transaction")
                    print("Please add nominal balance to continue this transaction")

        elif selectMenu == 3: 
                nominal = float(input("Enter the nominal balance:")) #enter the amount of money that will be save 
                checkDeposit = input("Confirmation: You will save the following nominal? " + str(nominal) + " ") #confirming to users

                if checkDeposit =="y":
                    atm.depositBalance(nominal)
                    print("Your Balance Now Is: Rp. " + str(atm.checkBalance()) + "\n")
                else:
                    break


        elif selectMenu == 4:
            verifyPin = int(input("Enter your Pin")) #user need to input their last code to confirm

            while verifyPin != int(atm.checkPin()): #if pin are wrong user need to try inputing again
                print("You entered the wrong pin, try again:")

                changePin = int(input("Please enter new pin:")) #enter new pin
                print("You have successfully changed your pin")
                verifynewPin = int(input("Enter new pin:")) #verfying new pin

                if verifynewPin == changePin: #if the value of both pin are true print success
                    print("New pin success")
                else:
                    print("Sorry, wrong pin. Try again")

        elif selectMenu == 5:
                print("Receipts are printed automatically when you exit. \n Please keep this receipt \n as proof of your transaction.")
                print("No. record:", random.randint(100000, 1000000))
                print("Date:", datetime. datetime.now())
                print("last Balance:", atm.checkBalance())
                exit()


