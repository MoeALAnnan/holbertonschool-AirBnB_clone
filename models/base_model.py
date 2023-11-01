#!/usr/bin/python3
""" Module for BaseModel """
import uuid
from datetime import datetime
import models
import models.engine.file_storage


"""Create BaseModel"""


class BaseModel():
    """ defines all common attributes/methods for other classes """
    def __init__(self, *args, **kwargs):
        if kwargs:
            self.updated_at = datetime.strptime(kwargs.get('updated_at'),
                                                '%Y-%m-%dT%H:%M:%S.%f')
            self.name = kwargs.get('name')
            self.my_number = kwargs.get('my_number')
            self.id = kwargs.get('id')
            self.created_at = datetime.strptime(kwargs.get('created_at'),
                                                '%Y-%m-%dT%H:%M:%S.%f')
        else:
            self.id = str(uuid.uuid4())
            self.created_at = datetime.now()
            self.updated_at = datetime.now()
            models.storage.new(self)

    def __str__(self):
        """String Doc"""
        print_str = "[{}] ({}) {}"
        return print_str.format(type(self).__name__, self.id, self.__dict__)

    def save(self):
        """ updates the current datetime and saves it"""
        self.updated_at = datetime.now()
        models.storage.save()

    def to_dict(self):
        """
        Returns a Dictionary with __dict__ method, adds
        a __class__ attribute value, converts created_at and
        updated_at datetimes
        """
        dic = (self.__dict__).copy()
        dic['__class__'] = type(self).__name__
        dic['created_at'] = self.created_at.isoformat()
        dic['updated_at'] = self.updated_at.isoformat()
        return dic
