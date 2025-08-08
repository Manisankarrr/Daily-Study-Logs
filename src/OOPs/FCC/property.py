
from datetime import datetime
class User:
    def __init__(self,username,email,password):
        self.username = username
        self._email = email
        self.password = password

    @property
    def email(self):
        print("Email accessed")
        return self._email
    
    @email.setter
    def email(self,new_email):
        if "@" and ".com" in new_email:
            self._email = new_email
        else:
            print("invalid")
    
    
user1 = User("Alice", "Alice@gmail.com ", "password123")
user1.email = "this is not email"
print(user1.email)