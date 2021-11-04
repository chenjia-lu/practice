class Employee:

    def __init__(self, first, last):
        self.first = first
        self.last = last

        # self.email = f'{first}.{last}@company.com'

    # Property method makes it so you don't need () after the method to call it. Can treat the method more like a field than a method
    @property
    def email(self):
        return f'{self.first}.{self.last}@company.com'

    @property
    def fullname(self):
        return f'{self.first} {self.last}'

    # Setter methods are method specific, makes it so that you can "set" the method like it is a field
    @fullname.setter
    # Need to use the same name as the original method
    def fullname(self, name):
        first, last = name.split(' ')
        self.first = first
        self.last = last

    # Deleter methods are method specific, makes it so that you can "del" attributes associated with the instance
    @fullname.deleter
    def fullname(self):
        print('Delete name')
        self.first = None
        self.last = None


emp_1 = Employee('Corey', 'Schafer')

print(emp_1.first)

emp_1.first = 'Jim'
print(emp_1.email)
# print(emp_1.email())

emp_1.fullname = 'John Smith'
# print(emp_1.fullname())
print(emp_1.fullname)

del emp_1.fullname

print(emp_1.first)
