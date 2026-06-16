class Employee:
    company = 'Google'  # Class Variable
    num_emp = 0         # Everytime an Instance is created __init__ runs so we can increment num_emp 
    raise_amount = 1.10
    def __init__(self,first,last,pay):
        self.first = first
        self.last = last
        self.pay = pay
        Employee.num_emp += 1       # Accessing Class Variable by using class
    
    def fullname(self):
        return '{} {}'.format(self.first , self.last)
    
    def pay_raise(self):            # This is a regular method which takes Instance as first argument (self)
        self.pay = int(self.pay * self.raise_amount)

    @classmethod        # Gives Class as the first argument (cls) !
    def change_raise(cls,amount):
        cls.raise_amount = amount

    @classmethod
    def from_string(cls,emp_string):    # Alternative Constructor for creating instances
        first , last , pay = emp_string.split('-')
        return cls(first,last,pay)  
    
    @staticmethod       # The argument is neither the class or the instance its just a regular function inside the class
    def is_weekday(day):    # Can be accessed the same i.e, Employee.is_workday()
        if day.weekday() < 5:  # 0 - Monday and 6 - Sunday
            return False
        return True
    
        



    
emp1 = Employee('Adarsh' , 'Bobade' , 50000)
emp2 = Employee('Dave' , 'mustaine' , 90000)
emp3 = Employee('James' , 'Hetfield' , 6000)
emp4 = 'John-don-80000'
emp4_new = Employee.from_string(emp4)
print(emp4_new.__dict__)

# print(emp1.fullname())
# print(emp1.company)
# print(emp1.__dict__)
# emp1.company = 'IBM'
# print(emp1.__dict__)   # Python created new Instance variable 'company' for emp1 !

# print(emp2.company)
# print(emp3.company)
# print(emp1.company)


# print(emp1.pay)
# emp1.pay_raise()        # Created a Method using both Class (raise_amount) and Instance (pay) variable
# print(emp1.pay)

# Employee.change_raise(1.20)     # We dont have to give class argument as it takes it by default !
# emp1.pay_raise()
# print(emp1.pay)
    
