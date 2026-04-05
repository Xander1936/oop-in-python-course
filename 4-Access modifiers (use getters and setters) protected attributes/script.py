# Accessing and Modifying Data
# 1. The traditional way: make the data private and use getter and setters:

class User:
    def __init__(self, username, email, password):
        self.username = username
        # "self._" the "_" here make the attribute protected -> The attribute is internal to the class
        self._email = email
        self._password = password
        
    def get_email(self):
        return self._email
    
    def clean_email(self):
        return self._email.lower().strip()
        
    
        
user1 = User("dantheman", "dan@gmail.com", "123")
print(user1.email)

user2 = User("batman", "bat@outlook.com", "abc") 

user1.email = "danny@gmail.com"
print(user1.email)