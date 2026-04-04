# Inheritance

# --> Parent Class or Base Class
# --> Child Class or Derived 


# --> single inheritance

class Animal:  # parent class
    
    parent_name = "Animal"
    def speak(self):
        print("Animal makes sound")

class Dog(Animal): # child class
    
    child_name = "Dog"
    def bark(self):
        print("Dog barks")
        

# d = Dog()
# d.speak()
# d.bark()
# print(d.parent_name)

# -- multiple inheritance

class Father: # Base Class
    def get_father_properties(self):
        print("Father ows a Bunglaw")

class Mother: # Base Class
    def get_monther_properties(self):
        print("Mother owns 1000GMS of Gold")
        
class Child(Father, Mother):  # Derived Class
    pass


# c = Child()
# c.get_father_properties()
# c.get_monther_properties()

# -- Multi-Level Inheritance

class GrandParent:
    def get_properties(self):
        print("Owns 100 crore property")
        
class Parent(GrandParent):  # Base and Derived
    pass

class Child(Parent):
    pass

# c = Child()
# print(c.get_properties())

# -- Hierarchial Inheritance

class Animal:  # parent class
    def speak(self):
        print("Animal makes sound") 

class Dog(Animal): # child class
    def bark(self):
        print("Dog barks")
    
class Cat(Animal): # child class
    def sound(self):
        print("Cat Meows")
        
    
# d = Dog()
# c = Cat()

# d.speak()
# c.speak()

# -- Super()

class Parent:
    def __init__(self, name: str):
        self.parent_name = name
        print("Parent Constructor")

class Child(Parent):
    def __int__(self, name: str):
        super().__init__(name)
        print("Child Constructor")
        

c = Child("Ram Charan")
print(c.parent_name)