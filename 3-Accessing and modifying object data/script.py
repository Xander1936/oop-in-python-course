class User:
    def __init__(self, username, email, password):
        self.username = username
        self.email = email
        self.password = password
        
    def say_hi_to_user(self, user):
        # self.username: fait appel à son propre username
        print(f"Sending message to {user.username}: Hi {user.username}, it's {self.username}") 
        
user1 = User("dantheman", "dan@gmail.com", "123")
print(user1.email)

user2 = User("batman", "bat@outlook.com", "abc")

user1.say_hi_to_user(user2) 

user1.email = "danny@gmail.com"
print(user1.email)