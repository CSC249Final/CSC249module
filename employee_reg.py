""" This module has a dictionary with pre-existing employees.
The application was designed to register new employees when they start
 their first day at work. The user will be able to 
 add, edit, remove, and view employees by ID or all."""

# Import abc to define the abstractmethod in the code
from abc import ABC, abstractmethod

##  CNYDI this is your section of the code to complete
## The names in the method to match those in the main function
# Employee class to manage employee information


class EmployeeRegistry:
    def __init__(self):
        # Pre-existing employees stored into the dictionary
        self.employees = {
            1001: {'first_name': 'Cyndi', 'last_name': 'Rue'},
            1002: {'first_name': 'Kayatha', 'last_name': 'Jerome'},
            1003: {'first_name': 'Asra', 'last_name': 'Khalid'},
            1004: {'first_name': 'Madison', 'last_name': 'Price'}
        }

    # Method to add a new employee
    def add_employee(self, first_name, last_name, id_number):
        self.employees[id_number] = {'first_name': first_name, 'last_name': last_name}

    # Method to view all employees in the dictionary
    def view_all_employees(self):
        if self.employees:
            print("List of all employees:")
            for id_number, employee in self.employees.items():
                print(f"ID: {id_number}, Name: {employee['first_name']} {employee['last_name']}")
        else:
            print("No employees found.")

##  MADISON this is your section of the code to complete
## The names in the method to match those in the main function
# Method to view employess by their ID number

    def view_employee_by_id(self, id_number):
        if id_number in self.employees:
            employee = self.employees[id_number]
            print(f"ID: {id_number}, Name: {employee['first_name']} {employee['last_name']}")
        else:
            print("Employee not found.")
# Method to edit employee information in the registry

    def edit_employee(self, employee_name, new_id_number):
        for id_number, employee in self.employees.items():
            if employee['first_name'] + ' ' + employee['last_name'] == employee_name:
                del self.employees[id_number]
                self.employees[new_id_number] = {'first_name': employee['first_name'], 'last_name': employee['last_name']}
                print(f"{employee_name}'s ID updated to {new_id_number}.")
                return
        print(f"No employee found with the name {employee_name}.")

##  ASRA this is your section of the code to complete
## The names in the method to match those in the main function
# Method to remove employee from the registry permanently

    def remove_employee(self, employee_name):
        for id_number, employee in self.employees.items():
            if employee['first_name'] + ' ' + employee['last_name'] == employee_name:
                del self.employees[id_number]
                print(f"{employee_name} has been removed from the registry.")
                return
        print(f"No employee found with the name {employee_name}.")

# Abstract base class for employee

class Employee(ABC):
    def __init__(self, first_name, last_name, id_number):
        self.first_name = first_name
        self.last_name = last_name
        self.id_number = id_number

# Class NewEmployee definition
class NewEmployee(Employee):
    def __init__(self, first_name, last_name, id_number):
        super().__init__(first_name, last_name, id_number)

##  MADISON this is your section of the code to complete
## The names in the method to match those in the main function
# Implementing the abstract method to get employee information
    def get_employee_info(self):
        return (f"Name: {self.first_name} {self.last_name}, ID: {self.id_number}")
