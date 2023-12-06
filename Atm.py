from datetime import date
today = date.today()  
  

print(f"Current day:", today.day,"-",today.month,"-",today.year,"\n******************************")
print

class Bank:

    def __init__(self,intial =0.00):
        self.bal=intial
        self.transaction(f'*****************{today.day}/{today.month}/{today.year}***********************')
        self.transaction(f'Before transaction balance amount: {self.bal}')

    def transaction(self,trans):
        with open("transaction_history.txt",'+a') as f:
            f.write(f"{trans} \n")

    def withdraw(self,amt):
        try:
            amt=float(amt)
        except ValueError:
            amt=0
        if amt:
            self.bal=self.bal-amt
            self.transaction(f"withdrew amount :{amt} and New Balance Amount :{self.bal}")


    def deposit(self,dep):
        try:
            dep=float(dep)
        except ValueError:
            dep=0
        if dep:
            self.bal=self.bal+dep
            self.transaction(f"Deposit amount :{dep} and New Balance Amount :{self.bal}")


    def totalbal(self):
        total=self.bal
        self.transaction(f'Available amount : {total}')



acc=Bank(float(input("enter the Balance in Atm Machine:")))  #object



while True:
    
    print(f"press 1: Balance\npress 2: Withdraw\npress 3: Deposit\n" )
    try:
        action=input("Press 1 or Press 2 or Press 3\nenter:")
        
    except KeyboardInterrupt:
        print("\n\nLeaving Atm,Visit Again ..\n")
        break
    

    if action  in ["1",'2',"3"]:
        if action == '1':
            acc.bal
            print("Available Balance",acc.bal)
            print("************************Visit Again****************************")

        elif action=='2':
            amt=input("enter the amount to withdraw:")
            acc.withdraw(amt)
            print(f"After,withdrawal amount {amt} Your Balance is :",acc.bal,'\n\n')
            print("************************Visit Again****************************")
        elif action=='3':

            dept=input("enter the amount to Deposit:")
            acc.deposit(dept)
            print(f"After,Deposited amount {dept} Your Balance is :",acc.bal,'\n\n')
            print("************************Visit Again****************************")


  
    
    

  


# print("intial bal:",acc.bal)
# acc.deposit(50)
# print("After depo bal:",acc.bal)
# acc.withdraw(10)
# print("After withdraw bal:",acc.bal)
# acc.totalbal()
# print("Available amount:",acc.bal)





      