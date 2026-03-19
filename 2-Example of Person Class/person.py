class Person:
    def __init__(self, name, age):
        # name and age are the attributes of the Person class
        self.name = name
        self.age = age
    # greet(self) is the method   
    def greet(self):
        print(f"Hello, my name is {self.name} and I am {self.age} years old.")

# Instanciation: create new objects named person1 and person2 
person1 = Person("Alexandre", 30)
person1.greet()

person2 = Person("Bob", 42)
person2.greet()