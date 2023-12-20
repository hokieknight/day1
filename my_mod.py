"""Module providing my values and functions."""
PI = 3.14159246

def myfunc():
    """Function printing test message."""
    print("myfunc processing...")

def empty_func():
    """empty func"""
    #pass

class User:
    """User Class"""
    def __init__(self, user_id, username):
        print("new user being created...")
        self.id = user_id
        self.username = username
        self.followers = 0
        self.following = 0

    def follow(self, user):
        """follow another user"""
        user.followers += 1
        self.following += 1

    def to_string(self):
        """to string"""
        return f"{self.id}, name = {self.username}, following = {self.following}, followers = {self.followers}"
