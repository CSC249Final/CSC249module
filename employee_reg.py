""" This module has a dictionary with pre-existing employees.
The main focus will be the employee's name and the ID number will be
selected at random by the employee. The employee will only be able
to be found with ID number but removing will need only the name."""

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
        pass
# Method to edit employee information in the registry

    def edit_employee(self, employee_name, new_id_number):
        pass

##  ASRA this is your section of the code to complete
## The names in the method to match those in the main function
# Method to remove employee from the registry permanently

    def remove_employee(self, employee_name):
        pass

# Abstract base class for employee

class Employee(ABC):
    pass

# Class NewEmployee definition
class NewEmployee(Employee):
    def __init__(self, first_name, last_name, id_number):
        pass

##  MADISON this is your section of the code to complete
## The names in the method to match those in the main function
# Implementing the abstract method to get employee information
    def get_employee_info(self):
        pass
