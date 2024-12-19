"""
1. City Infrastructure Management System
Objective: The aim of this assignment is to apply the concepts of Object-Oriented Programming in Python to build a simulated City Infrastructure Management System. 
This system will incorporate classes, objects, methods, and data structures to manage different aspects of a city, such as buildings, traffic, and events.

Task 1: Vehicle Registration System

Problem Statement: Create a Python class Vehicle with attributes registration_number, type, and owner. 
Implement a method update_owner to change the vehicle's owner. Then, create a few instances of Vehicle and demonstrate changing the owner.

Code Example: Provide a basic structure for the Vehicle class without methods.
class Vehicle:
    def __init__(self, reg_num, type, owner):
        self.registration_number = reg_num
        self.type = type
        self.owner = owner

Expected Outcome: Completion of the Vehicle class with the update_owner method and a demonstration script showing the creation of Vehicle objects and updating their owners.
"""
class Vehicle:
    def __init__(self, reg_num, type, owner):
        self.registration_number = reg_num
        self.type = type
        self.owner = owner
    
    def update_owner(self, owner):
      self.owner = owner

car = Vehicle(1111, "Kia", "Lauren")
truck = Vehicle(2222, "Ford", "Matt")
van = Vehicle(333, "Volkswagen", "Ryan")

print(f"Car Type: {car.type}, Owner: {car.owner}")
car.update_owner("Matt")
print(f"Car Type: {car.type}, Owner: {car.owner}")
print(f"Truck Type: {truck.type}, Owner: {truck.owner}")
truck.update_owner("Ryan")
print(f"Truck Type: {truck.type}, Owner: {truck.owner}")
print(f"Van Type: {van.type}, Owner: {van.owner}")
van.update_owner("Lauren")
print(f"Van Type: {van.type}, Owner: {van.owner}")

"""
Task 2: Event Management System Enhancement

Problem Statement: Extend an existing Event class by adding a feature to keep track of the number of participants. 
Implement a method add_participant that increases the count and a method get_participant_count to retrieve the current count.

Code Example: Basic Event class without participant tracking.
class Event:
    def __init__(self, name, date):
        self.name = name
        self.date = date
"""
class Event:
    def __init__(self, name, date):
        self.name = name
        self.date = date
        self.total_participant = 0

    def add_participant(self):
        self.total_participant += 1

    def get_participant_count(self):
        return self.total_participant

event = Event("Christmas Even", "12/24")
event2 = Event("Halloween", "10/31")

event.add_participant()
event.add_participant()
event2.add_participant()
event2.add_participant()
event2.add_participant()
event2.add_participant()
event2.add_participant()
print(event.get_participant_count())
print(event2.get_participant_count())