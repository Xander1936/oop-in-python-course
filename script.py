# Everything in Python is an object
# Class str -> object name
# Class int -> object age
# name = "Danny"
# age = 29

# print(name.upper())
# print(type(age))

class Dog:
    def __init__(self, name, breed):
        self.name = name
        self.breed = breed 
    
    def bark(self):
        print("Whoof whoof")
        
dog1 = Dog("Bruce", "Scottish Terrier")
dog1.bark()

dog2 = Dog("Freya", "Greyhound")
dog2.bark()

print(dog1.name +"_"+ dog1.breed)
print(dog2.name +"_"+ dog2.breed)