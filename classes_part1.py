# classes

class MyFirstClass:
    def greeting(self):
        return "Good Morning"
    
    def message(self):
        return "Hey, welcome to Python"


# obj1 = MyFirstClass()
# print(obj1.greeting())
# print(obj1.message())


# casing - camel, pascal and snake casing 

# --> goodMorningPrakash
# --> GoodMorningPrakash
# --> good_morning_prakash


# -- constructor method

class MyGreeting:
    def __init__(self, name: str):
        self.name = name  # intance variables
        print("Hey, contructer method is called")
        
    def greeting(self):
        print(f"Hello {self.name}, Good Morning!")
        

# ravi = MyGreeting("Ravi")
# ravi.greeting()


# teja = MyGreeting("Teja")
# teja.greeting()



class Employee:
    company_name = "Quant Cloud"
    
    def __init__(self, name: str):
        self.emp_name = name  # instance variable
    
    
emp1 = Employee("Rahul")
emp2 = Employee("Nikitha")

print(emp1.company_name)
print(emp1.emp_name)
print(emp2.company_name)
print(emp2.emp_name)