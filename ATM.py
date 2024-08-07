class Atm:
    def __init__(self):
        self.pin=None
        self.blc=0
        self.menu()
    
    def menu(self):
        print(""" Welcome To ATM\n1.To create Pin\n2.To check Balance\n3.To depoite Money\n4.To withdraw Money\n""")
        choice=input('Please Make Your Choice::')
        
        if choice == '1':
            self.createpin()
            print("pin created sucessfully")
            self.menu()
        elif choice == '2':
            self.showblc()
            print("balance show")
            self.menu()
        elif choice == '3':
            self.depamt()
            print("deposite sucessfully")
            self.menu()
        elif choice == '4':
            self.withamt()
            self.menu()
        else:
            print("invalid choice make correct choice again")
            self.menu()
    
    def createpin(self):
        self.pin=int(input("Create a new pin"))
    def showblc(self):
        enterpin=int(input("Enter Pin"))
        if(enterpin == self.pin):
            print(self.blc)
        else:
            print("invalid pin")
            self.menu()
    def depamt(self):
        enterpin=int(input("Enter Pin"))
        if(enterpin == self.pin):
            damt=int(input("Enter the deposite amt"))
            self.blc+=damt
        else:
            print("invalid pin")
            self.menu()
            
    def withamt(self):
        enterpin=int(input("Enter Pin"))
        if(enterpin == self.pin):
            wamt=int(input("Enter the withdrwal amt"))
            if self.blc < wamt:
                print("Not Sufficent money")
                self.menu()
            else:
                self.blc -= wamt
                print("withdrawl sucessfully")
        else:
            print("invalid pin")
            self.menu()   
atm=Atm()
        
