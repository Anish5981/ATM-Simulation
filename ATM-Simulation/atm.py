class Atm:
    #constructor
    def __init__(self):
        self.pin=""
        self.balance=0
        self.menu()
        
    def menu(self):
        user_input=input("""
        Hey! How can i help you?
        1.Press 1 to create pin
        2.Press 2 to change pin
        3.Press 3 to check balance
        4.Press 4 to withdraw
        5.Press any other key to exit
        
        """)
        if user_input=="1":
            #code to create pin
            self.Create_Pin()
        elif user_input=="2":
            #code to change pin
            self.Change_Pin()
            pass
        elif user_input=="3":
            #code to check balance
            self.Check_Balance()
            pass
        elif user_input=="4":
            #code to withdrawal
            self.Withdraw()
            pass
        else:
            print("Thankyou For Visiting!")
            exit()
        
    def Create_Pin(self):
        self.pin=(input("Enter your Pin: "))
        self.balance=int(input("Enter your Balance: "))
        print("Pin Created Successfully!")
        self.menu()
    def Change_Pin(self):
        old_pin=(input("Enter the Old Pin: "))
        if old_pin==self.pin:
            new_pin=(input("Enter the New Pin: "))
            self.pin=new_pin
            print("Pin has been Successfully Changed!")
            self.menu()
        else:
            print("Incorrect Pin!")
            self.menu()
        
    def Check_Balance(self):
        temp=(input("Enter the Pin: "))
        if temp==self.pin:
            print("your current balance in your account is", self.balance)
            self.menu()
        else:
            print("Incorrect Pin")
            self.menu()
    def Withdraw(self):
        passw=(input("Enter the pin: "))
        if passw==self.pin:
            amount=(int(input("Enter the amount to withdraw from your account")))
            if amount >self.balance:
                print("Insufficient Balance!")
	            
            else:
                #withdrawal code
                amount_after_deduction=self.balance-amount
                print("Your Balance After withdrawal is ",amount_after_deduction)
                self.balance=amount_after_deduction
            self.menu()
        else:
            print("Incorrect Pin!")
            self.menu()
        
        
        
        
        
        
anish=Atm()