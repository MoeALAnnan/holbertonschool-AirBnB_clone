#!/usr/bin/python3
""" Module for the Hbnb console """
import cmd
import json
from models import storage
from models.engine.file_storage import FileStorage
from models.__init__ import storage
from models.amenity import Amenity
from models.base_model import BaseModel
from models.city import City
from models.place import Place
from models.review import Review
from models.state import State
from models.user import User


class HBNBCommand(cmd.Cmd):
    """contains the entry point of the command interpreter """
    prompt = '(hbnb) '

    classes = {"Amenity": Amenity,
               "BaseModel": BaseModel,
               "City": City,
               "Place": Place,
               "Review": Review,
               "State": State,
               "User": User}

    def do_EOF(self, line):
        """ command to exit the program via CTRL+d """
        return True

    def emptyline(self):
        """ overrides the default behavior """
        pass

    def do_quit(self, line):
        """ command to exit the program """
        return True

    def do_create(self, line):
        """ command that creates a new instance """
        arg = line.split(" ")
        if arg[0] == "":
            print("** class name missing **")
        else:
            if arg[0] not in HBNBCommand.classes.keys():
                print("** class doesn't exist **")
            else:
                new_inst = HBNBCommand.classes[arg[0]]()
                new_inst.save()
                storage.save()
                print(new_inst.id)

    def do_show(self, line):
        """ Print instances """
        arg = line.split(" ")
        if arg[0] == "":
            print('** class name missing **')
        elif len(arg) == 1:
            print('** instance id missing **')
        else:
            if arg[0] not in HBNBCommand.classes.keys():
                print("** class doesn't exist **")
            else:
                try:
                    storage_all = storage.all()
                    obj = arg[0] + "." + arg[1]
                    instance = storage_all[f"{obj}"]
                    print(instance)
                except KeyError:
                    print('** no instance found **')

    def do_destroy(self, line):
        """ Deletes an instance """
        arg = line.split(" ")
        print(arg)
        if arg[0] == "":
            print("** class name missing **")
        else:
            if arg[0] not in HBNBCommand.classes.keys():
                print("** class doesn\'t exist **")
            elif len(arg) == 1:
                print("** instance id missing **")
            else:
                all_objs = storage.all()
                obj = arg[0] + "." + arg[1]
                if obj in all_objs.keys():
                    del all_objs[obj]
                    storage.save()
                else:
                    print("** no instance found **")

    def do_all(self, line):
        """Print all instances"""
        arg = line.split(" ")
        list = []
        storage_all = storage.all()
        if arg[0] == "":
            print(storage_all)
        else:
            try:
                eval(arg[0])
                for obj in storage_all:
                    key = obj.split('.')
                    if key[0] == arg[0]:
                        list.append(str(storage_all[obj]))
                print(list)
            except NameError:
                print('** class doesn\'t exist **')

    def do_update(self, line):
        """ command to add/update attributes """
        arg = line.split(" ")
        all_objs = storage.all()

        if arg[0] == "":
            print("** class name missing **")
        else:
            if arg[0] not in HBNBCommand.classes.keys():
                print("** class doesn't exist **")
            elif len(arg) == 1:
                print("** instance id missing **")
            elif len(arg) == 2:
                print("** attribute name missing **")
            elif len(arg) == 3:
                print("** value missing **")
            else:
                obj = arg[0] + "." + arg[1]
                if obj not in all_objs:
                    print("** no instance found **")
                else:
                    all_objs[obj].__dict__[arg[2]] = eval(arg[3])
                    storage.save()


if __name__ == '__main__':
    HBNBCommand().cmdloop()
