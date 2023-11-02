#!/usr/bin/python3
"""This module defines a base class for all models in our hbnb clone"""
import uuid
from datetime import datetime


class BaseModel:
    """A base class for all hbnb models"""
    def __init__(self, *args, **kwargs):
        """Instatntiates a new model"""
        if not kwargs:
            from models import storage
            self.id = str(uuid.uuid4())
            self.created_at = datetime.now()
            self.updated_at = datetime.now()
            storage.new(self)
        else:
            kwargs['updated_at'] = datetime.strptime(kwargs['updated_at'],
                                                     '%Y-%m-%dT%H:%M:%S.%f')
            kwargs['created_at'] = datetime.strptime(kwargs['created_at'],
                                                     '%Y-%m-%dT%H:%M:%S.%f')
            del kwargs['__class__']
            self.__dict__.update(kwargs)

    def __str__(self):
        """Returns a string representation of the instance"""
        return '[{}] ({}) {}'.format(self.__class__.__name__, self.id, self.__dict__)

    def save(self):
        """Updates updated_at with current time when instance is changed"""
        from models import storage
        # Update the update timestamp
        self.updated_at = datetime.now()
        # Call save method of storage
        storage.save()

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
