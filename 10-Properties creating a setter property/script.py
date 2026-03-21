# Accessing and Modifying Data
# 1. The traditional way: make the data private and use getter and setters:
# Name Mangled variables are private variables or attributes
# 2. Properties

# from datetime import datetime 

class User:
    def __init__(self, username, email, password):
        self.username = username
        # "self._" the "_" here make the attribute protected -> The attribute is internal to the class and can be access outside the class
        # 1. First Make the attribute private
        self._email = email
        self.password = password
    # 2. Add the property decorator -> @property turns the email method into a getter property
    # With @property we don4t worry about to create getter
    @property
    # 3. Create a method with the same name with the property we want to manipulate
    def email(self):
        print("Email accessed")
        return self._email
    
    @email.setter
    def email(self, new_email):
        if "@" in new_email:
            self._email = new_email
    

user1 = User("dantheman", "dan@gmail.com", "123")
user1.email = "this is not an email" 
print(user1.email)

