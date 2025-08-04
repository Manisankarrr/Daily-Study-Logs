# Accessing and Modifying Data:
# 1. The traditional way: make the data private and use getters and
#setters:
# __email = name mangles the variable to _User__email

from datetime import datetime
class User:
    def __init__(self,username,email,password):
        self.username = username
        self._email = email
        self.password = password

    def clean_email(self):
        return self._email.lower().strip()
    
    def get_email(self):
        print(f"Email accessed at {datetime.now()}")
        return self._email
    
    def set_email(self, new_email):
        if "@" and ".com" in new_email:
            self._email = new_email

    
user1 = User("Alice", " AliCe@gmail.com ", "password123")

# print(user1.__email) # no

print(user1.clean_email())# yes

user1.set_email("manish.u2416@gmail.com")
print(user1.get_email())

user1.set_email("g@mail.com")
print(user1.get_email())