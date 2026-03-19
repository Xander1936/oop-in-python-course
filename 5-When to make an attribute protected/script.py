# Accessing and Modifying Data
# 1. The traditional way: make the data private and use getter and setters:

class User:
    def __init__(self, username, email, password):
        self.username = username
        # "self._" the "_" here make the attribute protected -> The attribute is internal to the class -> it's can be accessed outside
        self._email = email
        self._password = password
        
    def get_email(self):
        return self._email
    
    def clean_email(self):
        return self._email.lower().strip()

user1 = User("dantheman", "Dan@gmail.com ", "123")

print(user1._email)
print(user1.clean_email())