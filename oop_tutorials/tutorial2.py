# Tutorial 2

class Employee:
    # Class attributes/variables
    raise_amount = 1.04
    num_of_emps = 0

    # Init function with instance attributes/variables; runs every time new instance is created
    def __init__(self, first, last, pay):
        self.first = first
        self.last = last
        self.pay = pay
        self.email = first + "." + last + "@company.com"

        Employee.num_of_emps += 1

    # Methods
    def fullname(self):
        return '{} {}'.format(self.first, self.last)

    def apply_raise(self):
        self.pay = int(self.pay * self.raise_amount) #could also use Employee.raise_amount if we want to force class attribute instead of instance attribute

print(Employee.num_of_emps)

emp_1 = Employee('Corey', 'Schafer', 60000)
emp_2 = Employee('Test', 'User', 50000)

print(Employee.num_of_emps)

# print(emp_1.pay)
# emp_1.apply_raise()
# print(emp_1.pay)


# print(emp_1.__dict__)
# print(Employee.__dict__)
#
# Employee.raise_amount = 1.05
#
# print(emp_1.raise_amount)
# print(emp_2.raise_amount)
# print(Employee.raise_amount)
#
# emp_1.raise_amount = 1.06
# print(emp_1.raise_amount)
# print(emp_2.raise_amount)
# print(Employee.raise_amount)
#
# print(emp_1.__dict__)
