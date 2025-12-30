#!/usr/bin/env python
class SecurePlant:
    def is_valid(self, val: int):
        if val < 0:
            return False
        else:
            return True
    def get_height(self):
        return self.height
    def get_age(self):
        return self.age
    def set_age(self, age: int):
        if self.is_valid(age) == True:
            self.age = age
            print(f"Age updated: {age} days [OK]")
        else:
            print(f"Invalid operation attempted: age {age} days [REJECTED]")
            print("Security: Negative age rejected")
    def set_height(self, height: int):
        if self.is_valid(height) == True:
            self.height = height
            print(f"Height updated: {height}cm [OK]")
        else:
            print(f"Invalid operation attempted: height {height}cm [REJECTED]")
            print("Security: Negative height rejected")
    def __init__(self, name: str, height: int, age: int):
        self.name = name
        if self.is_valid(height) == True:
            self.height = height
        else:
            print(f"Invalid operation attempted: height {height}cm [REJECTED]")
            print("Security: Negative height rejected")
            print("Action taken: height set to 0")
            self.height = 0
        if self.is_valid(age) == True:
            self.age = age
        else:
            print(f"Invalid operation attempted: age {age} days [REJECTED]")
            print("Security: Negative age rejected")
            print("Action taken: age set to 0")
            self.age = 0
print("=== Garden Security System ===")
rose = SecurePlant("Rose", 45, 9)
print(f"Plant created: {rose.name}")
rose.set_height(25)
rose.set_age(30)
print()
rose.set_height(-25)
print()
print(f"Current plant: {rose.name} ({rose.get_height()}cm, {rose.get_age()} days)")