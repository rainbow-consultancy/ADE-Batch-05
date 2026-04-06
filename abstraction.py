# Abstraction

from abc import ABC, abstractmethod

class Vehicle(ABC):  
    @abstractmethod
    def start(self):
        pass
    
class Car(Vehicle):
    def start(self):
        print("Car Started")
        
class Bike(Vehicle):
    def stop(self):
        print("Bike Stopped")
    
    def start(self):
        print("Bike Started")
        

c = Car()
c.start()

b = Bike()
b.stop()

v = Vehicle()