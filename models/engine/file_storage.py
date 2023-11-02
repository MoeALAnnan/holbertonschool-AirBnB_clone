#!/usr/bin/python3
""" Module with class FileStorage """
import json
from models.base_model import BaseModel


class FileStorage:
    """ serializes instances to a JSON file """
    """ and deserializes JSON file to instances """
    __file_path = 'file.json'
    __objects = {}

    def all(self):
        """ return the dictionary __objects """
        return self.__objects

    def new(self, obj):
        """ sets in __objects the obj with key <obj class name>.id """
        """self.__objects = '{}.{}'.format(self.__class__.__name__, self.id)"""
        key = obj.__class__.__name__ + '.' + obj.id
        FileStorage.__objects[key] = obj

    def save(self):
        """ serializes __objects to the JSON file """
        dict = {}
        for key, value in self.__objects.items():
            dict[key] = value.to_dict()
        with open(self.__file_path,"w", encoding="utf-8") as f:
            json.dump(dict, f)

    def reload(self):
        """ deserializes the JSON file to __objects """
        try:
            with open(self.__file_path, "r", encoding="utf-8") as f:
                for key, value in json.load(f).items():
                    self.__objects[key] = eval(value['__class__'])(**value)
        except FileNotFoundError:
            pass