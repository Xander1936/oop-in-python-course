# Accessing and Modifying Data
# 1. The traditional way: make the data private and use getter and setters:
# Name Mangled variables are private variables or attributes
# 2. Properties

from datetime import datetime 

class User:
    def __init__(self, username, email, password):
        self.username = username
        # "self._" the "_" here make the attribute protected -> The attribute is internal to the class and can be access outside the class
        self._email = email
        self.password = password
        
    def get_email(self):
        print(f"Email accessed at {datetime.now()}")
        return self._email
    
    def set_email(self, new_email):
        if "@" in new_email:
            self._email = new_email
    

user1 = User("dantheman", "dan@gmail.com", "123") 
print(user1.get_email())

user1.set_email("danny@outlook.com")
print(user1.get_email())

# user2 = User("superman", "clark@gmail.com", "123") 
# print(user2.get_email())

# user2.set_email("1223@55336s.com")
# print(user2.get_email())

user2 = User("ironman", "tony@gmail.com", "124")
user2.email = "this is not an email"
print(user2.email)