class Employee:
    raise_amt = 1.04

    def __init__(self, first, last, pay):
        self.first = first
        self.last = last
        self.pay = pay

        self.email = f'{first}.{last}@company.com'

    def fullname(self):
        return f'{self.first} {self.last}'

    def apply_raise(self):
        self.pay = int(self.pay * self.raise_amt)

    # Special methods are also called Dunder because they were surrounded by double underscores
    def __repr__(self):
        # Usually a string that gives information about how to recreate the instance
        return f"Employee('{self.first}', '{self.last}', {self.pay})"

    def __str__(self):
        return f"{self.fullname()} - {self.email}"

    def __add__(self, other):
        return self.pay + other.pay

    def __len__(self):
        # Don't want to throw error but also don't know how to handle, defaults to the other object's method
        # return NotImplemented
        return len(self.fullname())


emp_1 = Employee('Corey', 'Schafer', 60000)
emp_2 = Employee('Test', 'Employee', 50000)

# print(emp_1)
#
# # Used for debugging and logging (for other developers)
# print(repr(emp_1))
# print(emp_1.__repr__())
# # Readable version (for end user)
# print(str(emp_1))
# print(emp_1.__str__())

# # Rewrite a dunder add method to define the '+' operation
# print(emp_1 + emp_2)
#
# # Rewrite a dunder len method to define the len() method
# print(len(emp_2))

