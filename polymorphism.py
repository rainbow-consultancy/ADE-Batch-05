
# Method Overriding

class Animal:
    def sound(self):
        print("Animal makes sound")
        
    def get_name(self):
        print("Animal name")
    
class Dog(Animal):
    def sound(self):
        print("Dog Barks!")

class Cat(Animal):
    def sound(self):
        print("Cat Meows!")
        
a = Animal()
b = Dog()
c = Cat()

# c.sound()
# c.get_name()


# Method Overloading

# def add(a, b):
#     return a + b

def add(a, b, c=0):
    return a + b + c


# print(add(10, 20))
# print(add(10,20,30))


class Payments:
    def pay(self):
        pass
    
class CreditCard(Payments):
    def pay(self):
        print("Paid using cc")
    
class UPI(Payments):
    def pay(self):
        print("Paid using upi")

def process_payment(method):
    method.pay()
    
process_payment(CreditCard())
process_payment(UPI())