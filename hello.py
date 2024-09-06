import sys
n = float(input("first number "))

if n > 0:
    print("n is positive")
elif n < 0:
    print("n is negative")
else:
    print("n is zero")

""" Data Structure : 
list - sequence of mutable values 
tuple - sequence of immutable values (cant change)
set - collection of unique values
dict - collection of key-value pairs
"""
s = set()
s.add(1)
s.add(2)
s.add(3)
s.add(4)
s.add(1)
print(s) #unique values
s.remove(1)

#format string
print(s, f"The set has {len(s)} element")
coordinateX = 10.0
coordinateY = 20.0
coordinate = (coordinateX, coordinateY)



#decorators

def announce(f):
    def wrapper():
        print("About to run the function ..")
        f()
        print("Done with the function.")
    return wrapper

@announce
def hello():
    print("Hello, world!")


people = [
    {"name": "Rasha", "house": "Gryfiindor"},
    {"name": "Harry", "house": "Ravenclaw"},
    {"name": "Draco", "house": "Slytherin"},
]

def f(person):
    return person["name"]

try:
    x = int(input("x: "))
    y = int(input("y: "))
except ValueError:
    print("Error: Invalid input.")
    sys.exit(1)


try:
    result = x / y
except ZeroDivisionError:
    print("Error: cannot divide by 0 .")
    sys.exit(1)
print(f"{x} / {y} = {result}")
if __name__ == '__main__':
    hello()
    people.sort(key=f) # the way of the sorting key by function sort by letter
    print(people)
    people.sort(key=lambda person: person["house"]) # sort by lambda
    pass