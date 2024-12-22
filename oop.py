class Customer:
    def __init__(self, name, balance):  
        self.name = name
        self.balance = balance
        print("The	init	method was called")

customer = Customer("Lara de Silva" , 100) 
print(customer.name) 
print(customer.balance) 


# Constructors with default values (balance)

class Customer:
    def	__init__(self, name, balance=0):  
        self.name = name
        self.balance = balance
        print("The	init	method was called")
        

customer = Customer("Lara de Silva") # <-- don't specify balance explicitly  print(cust.name)
print(customer.balance) # <-- attribute is created anyway


##Class other special functions

class Customer:
    def	__init__(self, name, balance=0):  
        self.name = name
        self.balance = balance
        print("The	init	method was called")
        
    def __str__(self):
        return 'Customer : ' +str(self.name)+ ' , balance: ' + str(self.balance) 
    
    def __add__(self, other): 
        return Customer("Test_Customer",self.balance + other)

customer = Customer("Lara de Silva") 
print(customer.balance) 
print(customer)

c2 = customer + 230
print(c2.balance)


