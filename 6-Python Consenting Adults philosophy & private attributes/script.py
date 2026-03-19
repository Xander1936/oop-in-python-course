# Accessing and Modifying Data
# 1. The traditional way: make the data private and use getter and setters:
# Name Mangled variables are private variables or attributes 

class User:
    def __init__(self, username, email, password):
        self.username = username
        # "self.__" the "__" here make the attribute private -> The attribute is internal to the class and cannot be accessed outside the class
        self.__email = email
        self.__password = password
        
    def get_email(self):
        return self.__email
    
    def clean_email(self):
        return self.__email.lower().strip()

user1 = User("dantheman", "Dan@gmail.com ", "123")

print(user1.__email)
print(user1.clean__email()+"_"+user1.__password)

# The "Consenting Adults" Philosophy
