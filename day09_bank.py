#ans q34:
#        class is a blueprint or template, while an instance (also called an object) is a specific thing created from that blueprint.
#         supposeCar is the class.car1 and car2 are instances (objects) of the Car class.
#ans q35:
#       In Python, self is a reference to the current instance (object) of a class. 
#       It allows a method to access and modify that object's attributes and call its other methods.
#       self is a convention, not a reserved keyword, but it should almost always be used as the first parameter name for instance methods.
#ans q36:
#        __init__ is a special method (often called the constructor, although technically it's an initializer) 
#        that Python automatically calls whenever you create a new object from a class.
#        Yes. A class does not have to define an __init__ method. Using __init__ makes object creation cleaner and ensures each object is initialized consistently.
#ans q37:
#        An instance variable belongs to an individual object. Each object has its own copy.
#        class Student:
#        def __init__(self, name):
#        self.name = name   # Instance variable
#        s1 = Student("Alice")
#        s2 = Student("Bob")
#        print(s1.name)  # Alice
#        print(s2.name)  # Bob
#        A class variable belongs to the class itself. It is shared by all objects created from that class.
#        class Student:
#        school = "ABC School"   # Class variable
#        s1 = Student()
#        s2 = Student()
#        print(s1.school)  # ABC School
#        print(s2.school)  # ABC School

from datetime import datetime
class BankAccount:
    next_account_number = 1001
    def __init__(self, owner, balance=0.0, currency="USD"):
        self.owner= owner
        self.account_number= BankAccount.next_account_number
        BankAccount.next_account_number += 1
        
        self.balance = balance
        self.currency = currency
        self.history = []
    def deposit(self, amount):
        if amount < 0:
            raise ValueError("Deposit amount shloud positive.")
        self.balance += amount
        transaction = {"type": "Deposit", "amount": amount, "timestamp": datetime.now().strftime("%Y-%m-%d %H:%M:%S"), "balance": self.balance}
        self.history.append(transaction)
        print(f"Successfully Deposit: {amount} {self.currency}.")
    def withdraw(self, amount):
        if amount < 0:
            raise ValueError("amount shloud be positive.")
        if amount > self.balance:
            raise ValueError("Insufficient balance.")
        self.balance -= amount
        transaction = {"type": "Withdrawal", "amount": amount, "timestamp": datetime.now().strftime("%Y-%m-%d %H:%M:%S"), "balance": self.balance}
        self.history.append(transaction)
        print(f"Successfuly Withdraw: {amount} {self.currency}.")
    def transfer(self, target_account, amount):
        if amount < 0:
            raise ValueError("transfer ammount must be positive.")
        if amount > self.balance:
            raise ValueError("Insufficient balance for Transfer.")
        self.balance -= amount
        self.history.append({"type": "Transfer Sent", "amount": amount, "timestamp": datetime.now().strftime("%Y-%m-%d %H:%M:%S"), "balance": self.balance})
        target_account.balance += amount
        target_account.history.append({"type": "Transfer Received:", "amount": amount, "timestamp": datetime.now().strftime("%Y-%m-%d %H:%M:%S"), 
        "balance": target_account.balance})
        print(f"Transfered: {amount} {self.currency} to {target_account.owner}")
    def get_balance(self):
        return self.balance
    def get_statement(self):
        print("\n" + "-" * 50)
        print(f"Owner: {self.owner}")
        print(f"account number: {self.account_number}")
        print(f"Balance: {self.balance} {self.currency}")
        print("-" * 50)
        
        print("Transactions:")
        print("-" * 70)
        print(f"{'Type':<18}{'Amount':<12}{'Time':<25}{'Balance'}")
        print("-" * 70)
        
        for t in self.history:
            print(f"{t['type']:<18}{t['amount']:<12}{t['timestamp']:<25}{t['balance']}")
            print("-" * 70)
    def __str__(self):
        return f"{self.owner} | Account #{self.account_number} | Balance :{self.balance} {self.currency}"
             
        
        
        
        
account1 = BankAccount("Alice", 1000)
account2 = BankAccount("Bob", 500)

print(account1.owner)
print(account1.account_number)
print(account1.balance)

print(account2.owner)
print(account2.account_number)
print(account2.balance)
account = BankAccount("Alice", 1000)

account.deposit(500)

print(account.balance)
print(account.history)

account = BankAccount("Alice", 1000)

account.withdraw(300)

print(account.balance)
print(account.history)

acc1 = BankAccount("Alice", 1000)
acc2 = BankAccount("Bob", 500)

acc1.transfer(acc2, 300)

print(acc1.balance)
print(acc2.balance)

acc = BankAccount("Alice", 1000)
acc.deposit(500)
acc.withdraw(200)
acc.get_statement()

acc = BankAccount("Alice", 1000)
print(acc)