# Easy 1
def calculate_average(numbers):
    if not numbers:
        return 0
    return sum(numbers) / len(numbers)

# Easy 2
def greet_user(name, greeting="Hello"):
    return f"{greeting}, {name}!"

# Medium 1
def calculate_total(*prices,discount=0):
    total=sum(prices)
    if discount>0:
        total-=total*(discount/100)
    return total

# Medium 2
def create_multiplier(value):
    def multiply(number):
        return number*value
    return multiply

# Hard 1
def power(number,exponent):
    if exponent==0:
        return 1
    
    if exponent%2==0:
        return power((number*number),exponent//2)
    else:
        return number*power((number*number),exponent//2)

# Hard 2
def compose(*functions):
    def single_functions(value):
        for i in reversed(functions):
            value=i(value)
        return value
    return single_functions

#Test Cases:

# Easy 1:
print(calculate_average([5, 10, 15, 20]))  # Should return 12.5
print(calculate_average([]))  # Should return 0

# Easy 2:
print(greet_user("Alice"))  # Should return "Hello, Alice!"
print(greet_user("Bob", "Hi"))  # Should return "Hi, Bob!"

# Medum 1:
print(calculate_total(10, 20, 30))  # Should return 60
print(calculate_total(10, 20, 30, discount=10))  # Should return 54 (10% off)

# Medium 2:
double = create_multiplier(2)
triple = create_multiplier(3)
print(double(5))  # Should return 10
print(triple(5))  # Should return 15

# Hard 1:
print(power(2, 10))  # Should return 1024
print(power(3, 4))   # Should return 81

# Hard 2:
def add_one(x): return x + 1
def double(x): return x * 2
def square(x): return x ** 2
f = compose(square, double, add_one)
print(f(3))  # Should compute square(double(add_one(3))) = square(double(4)) = square(8) = 64
