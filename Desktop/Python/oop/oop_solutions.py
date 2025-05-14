# Easy 1
class Rectangle_Easy:
    def __init__(self,height,width):
        self.height=height
        self.width=width
    
    def area(self):
        return (self.height)*(self.width)
    def perimeter(self):
        return 2*(self.height+self.width)


# Easy 2
class Counter:
    def __init__(self):
        self.value=0
    
    def increment(self):
        self.value+=1
    def decrement(self):
        self.value-=1
    def reset(self):
        self.value=0


# Medium 1
class Vehicle:
    def __init__(self,make,model,year):
        self.make=make
        self.model=model
        self.year=year
class Car(Vehicle):
    def __init__(self, make, model, year,doors,fuel_type):
        super().__init__(make, model, year)
        self.doors=doors
        self.fuel_type=fuel_type


# Medium 2
class BankAccount:
    def __init__(self,account_number,initial_balance=0):
        self.__account_number=account_number
        self.__balance=initial_balance
    
    def deposit(self,amount):
        if amount>0:
            self.__balance+=amount
    
    def withdraw(self,amount):
        if amount>0:
            if amount<self.__balance:
                self.__balance-=amount
    
    def get_balance(self):
        return self.__balance
    
    def get_account_number(self):
        return self.__account_number


# Hard 1
from abc import ABC,abstractmethod
import math

class Shape(ABC):
    @abstractmethod
    def area(self):
        pass

class Circle(Shape):
    def __init__(self,radius):
        self.radius=radius
    
    def area(self):
        return math.pi*(self.radius**2)

class Rectangle(Shape):
    def __init__(self,length,breadth):
        self.length=length
        self.breadth=breadth
    
    def area(self):
        return self.length*self.breadth
    
class Triangle(Shape):
    def __init__(self,a,b,c):
        self.a=a
        self.b=b
        self.c=c

    def area(self):
        s=(self.a+self.b+self.c)/2
        return math.sqrt(s*(s-self.a)*(s-self.b)*(s-self.c))



#Test Cases:

# Easy 1:
rect = Rectangle_Easy(5, 10)
print(rect.area())  # Should return 50
print(rect.perimeter())  # Should return 30

# Easy 2:
counter = Counter()
counter.increment()
counter.increment()
print(counter.value)  # Should return 2
counter.decrement()
print(counter.value)  # Should return 1
counter.reset()
print(counter.value)  # Should return 0

# Medum 1:
car = Car("Toyota", "Corolla", 2020, 4, "Gasoline")
print(car.make)  # Should return "Toyota"
print(car.doors)  # Should return 4

# Medium 2:
account = BankAccount("123456", 1000)
print(account.get_balance())  # Should return 1000
account.deposit(500)
print(account.get_balance())  # Should return 1500
account.withdraw(200)
print(account.get_balance())  # Should return 1300
print(account.get_account_number())  # Should return "123456"

# Direct access should not be allowed
try:
    account._balance = 2000  # This should be discouraged or prevented
except AttributeError:
    print("Cannot directly access private attribute")

# Hard 1:
circle = Circle(5)
rectangle = Rectangle(4, 6)
triangle = Triangle(3, 4, 5)

shapes = [circle, rectangle, triangle]
for shape in shapes:
    print(f"{shape.__class__.__name__} area: {shape.area()}")

# Hard 2:
