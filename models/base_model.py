#!/usr/bin/python3
"""This module defines a base class for all models in our hbnb clone"""

import uuid
import datetime


class BaseModel:
    """A base class for all hbnb models"""
    def __init__(self, *args, **kwargs):
        """Instantiates a new model either from a dictionary representation
        or from a new instance.
        """
        if kwargs:
            for key, value in kwargs.items():
                if key != '__class__':
                    if key == 'created_at' or key == 'updated_at':
                        value = datetime.datetime.strptime(
                            value,
                            '%Y-%m-%dT%H:%M:%S.%f'
                            )
                    setattr(self, key, value)
        else:
            # Generate a unique id and convert to string
            self.id = str(uuid.uuid4())
            # Set creation timestamp
            self.created_at = datetime.datetime.now()
            # Set initial update timestamp to creation timestamp
            self.updated_at = self.created_at

    def __str__(self):
        """Returns a string representation of the instance"""
        string_representation = "[{}] ({}) {}"
        return string_representation.format(
            self.__class__.__name__,
            self.id, self.__dict__)

    def save(self):
        """Updates updated_at with current time when instance is changed"""
        # Update the update timestamp
        self.updated_at = datetime.datetime.now()

    def to_dict(self):
        """Convert instance into dict format"""
        # Copy the instance attributes
        dictionary = self.__dict__.copy()
        # Add class name to the dictionary
        dictionary['__class__'] = self.__class__.__name__
        # Convert created_at to ISO format
        dictionary['created_at'] = self.created_at.isoformat()
        # Convert updated_at to ISO format
        dictionary['updated_at'] = self.updated_at.isoformat()
        return dictionary
