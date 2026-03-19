# Accessing and Modifying Data
# 1. The traditional way: make the data private and use getter and setters:
# Name Mangled variables are private variables or attributes 

class User:
    def __init__(self, username, email, password):
        self.username = username
        # "self._" the "_" here make the attribute protected -> The attribute is internal to the class and can be access outside the class
        self._email = email
        self.password = password
        
    def get_email(self):
        return self._email
    
    def set_email(self, new_email):
        self._email = new_email
    

user1 = User("dantheman", "dan@gmail.com", "123") 
print(user1.get_email())

user1.set_email("danny@outlook.com")
print(user1.get_email())