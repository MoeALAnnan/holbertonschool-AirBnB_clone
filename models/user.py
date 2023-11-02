#!/usr/bin/python3
"""A class representing a User"""
from models.base_model import BaseModel


class User(BaseModel):
    """A class representing a User"""

    def __init__(self, *args, **kwargs):
        """Initialize a User instance"""
        super().__init__(*args, **kwargs)
        self.email = kwargs.get('email', '')
        self.password = kwargs.get('password', '')
        self.first_name = kwargs.get('first_name', '')
        self.last_name = kwargs.get('last_name', '')

    def __str__(self):
        """Return a string representation of the User instance"""
        return "[User] ({}) {}".format(self.id, self.__dict__)
