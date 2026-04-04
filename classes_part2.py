# class methods

class Employee:
    company = "Quant Cloud"
    
    @classmethod
    def change_company(cls, new_name: str):
        cls.company = new_name
        
    
# Employee.change_company("Quant Cloud Technologies")
# print(Employee.company)

# emp = Employee()
# emp.company = "XYZ"
# print(emp.company)
        
# Static Method

class Utils:
    @staticmethod
    def add(a, b):
        return a + b
    
# print(Utils.add(10, 30))


# ----------------------------------------------

# OOP'S - Object Oriented Programing

# 1. Encapsulation
# 2. Inheritence
# 3. Polymorphisam
# 4. Abstraction


class BankAccount:
    def __init__(self, balance: int):
        self.__balance = balance
      
    def get_balance(self):
        return self.__balance  

# bnk = BankAccount(200)
# # print(bnk.__balance) you can't access a private varaible
# print(bnk.get_balance()) # private variables can be accessed only by its own class objects


class BankAccount:
    def __init__(self, balance: int):
        self.__balance = balance
        print(f"Current Balance: {self.__balance}")
        
    def deposit(self, amount: int):
        if amount > 0:
            self.__balance += amount
            print(f"Deposit Successful, Current Balance: {self.__balance}")
    
    def withdraw(self, amount: int):
        if amount <= self.__balance:
            self.__balance -= amount 
            print(f"Withdram of {amount} is successful, current balance is {self.__balance}")
        else:
            print(f"Something went wrong, Insufficient Balance")


# bnk = BankAccount(4500)
# bnk.deposit(1000)
# bnk.withdraw(500)

class BankAccount:
    def __init__(self, balance: int):
        self.__balance = balance
        print(f"Current Balance: {self.__balance}")
    
    def __calculate_interest(self):
        return self.__balance * 0.05
    
    def show_balance_with_interest(self):
        interest = self.__calculate_interest()
        print(f"interest generated: {interest}")
        print(f"Total Current Balance with Interest: {self.__balance + interest}")
    

bnk = BankAccount(30000)
bnk.show_balance_with_interest()
# bnk.__calculate_interest()


