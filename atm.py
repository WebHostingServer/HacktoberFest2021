print("\t\t\t\t WELCOME TO SBI ATM")

curr_amt = 200000 
pin = int(input("\nEnter your 4-digit pin : "))

while(True):
    if pin == 2611 :
        print("\n\t 1. Withdraw money ")
        print("\t 2. Deposit money ")
        print("\t 3. Balance enquiry ")
        print("\t 4. Exit ")

        ch = int(input("\nChoose option(1-4) :"))
        while(ch):
            if ch == 1:
                amt = int(input("Enter amount :"))
                if amt > curr_amt :
                    print("Transaction denied - Withdrawal amount exceeds current amount")
                else:     
                    curr_amt -= amt
                    print("***** Transaction is Successful *****")
                    break
            
            elif ch == 2:
                amt = int(input("Enter amount :"))
                curr_amt += amt
                print("***** Transaction is Successful *****")
                break
                
            elif ch == 3:
                print("Current balance : ",curr_amt)
                break
            
            elif ch == 4:
                print("THANK YOU FOR VISITING")
                exit(0)
    else:
        print("Incorrect pin!!! ")
        exit()
