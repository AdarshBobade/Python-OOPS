class Employee:
    company = 'Google'  # Class Variable
    num_emp = 0         # Everytime an Instance is created __init__ runs so we can increment num_emp 
    raise_amount = 1.10
    def __init__(self,first,last,pay):
        self.first = first
        self.last = last
        self.pay = pay
        self.email = first + '.' + last + '@gmail.com'
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
# print(emp4_new.__dict__)

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
    
class Developer(Employee) :    # Creating a subclass from the Employee class (Parent) depicting Inheritance
    raise_amount = 1.50
    def __init__(self,first,last,pay,prog_lang):
        super().__init__(first,last,pay)    # Borrow __init__ from Employee class 
        # The moment __init__ is defined in child class , Parent's __init__ is dead , we have to use it explicitly using super()!
        self.prog_lang = prog_lang
    

dev1 = Developer('John' , 'Lennon' , 23450 , 'Python')
dev2 = Developer('Kurt' , 'Cobain' , 500 , 'C++')
dev3 = Developer('Bon', 'Jovi',750 , 'SQL')

class Manager(Employee):
    def __init__(self,first,last,pay,employees = None):
        super().__init__(first,last,pay)
        if employees is None:
            self.employees = []
        else:
            self.employees = employees
    
    def add_emp(self,emp):
        if emp not in self.employees:
            self.employees.append(emp)
        
    def print_emp(self):
        for emp in self.employees:
            print('-->',emp.fullname())
        

# dev1.pay_raise()    # So it used Employee class method {.pay_raise()} but with its own modified variable i.e, raise_amount = 1.50
# print(dev1.pay)
print(dev3.email)

mng1 = Manager('Steve','Smith', 80000,[dev1,dev2,dev3])
mng1.add_emp(emp1)
mng1.print_emp()


# Dunder Methods (Double Underscore methods)
# PYTHON IS ONE GIGANTIC OBJECT ORIENTED SYSTEM !
# print(a+b) --> print((a).__add__(b)) ; __add__() is a dunder method
# print('abc') --> print('abc'.__str__()) ; 'abc' is an Object of class str !
class Person:
    def __new__(cls,first,last,age):
        print("Creating object...")
        return super().__new__(cls)

    def __init__(self,first,last,age):
        print("Initializing object...")
        self.first = first
        self.last = last
        self.age = age
        # self.email = first + '.' + last + '@gmail.com'

    @property   # Property decorator makes the method act like normal attribute
    def email(self):
        return '{}.{}@gmail.com'.format(self.first , self.last)
    
    # @property
    def fullname(self):
        return '{} {}'.format(self.first, self.last)
    
    # @fullname.setter    # Now it'll take fullname and break it into first and last 
    # def fullname(self,name):
    #     first , last = name.split(' ')
    #     self.first = first
    #     self.last = last

    
    def __repr__(self):
        return "Employee('{}','{}',{})".format(self.first, self.last, self.age)
    
    def __str__(self):
        return "{} - {}".format(self.fullname() , self.email)
    

    

p1 = Person('Adarsh','Bobade',20)
print(p1)




