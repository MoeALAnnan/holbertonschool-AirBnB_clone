#!/usr/bin/python3
""" Console Module """

import cmd
import models
from models.base_model import BaseModel


class HBNBCommand(cmd.Cmd):
    """ Console Module """
    prompt = '(hbnb) '

    def do_quit(self, arg):
        """Exit the program"""
        return True

    def do_EOF(self, arg):
        """Exit the program"""
        print("")
        return True

    def help_quit(self):
        print("Quit command to exit the program")

    def emptyline(self):
        pass

    def do_create(self, arg):
        """Create a new instance of BaseModel or User"""
        if not arg:
            print("** class name missing **")
        else:
            try:
                new_instance = eval(arg)()
                new_instance.save()
                print(new_instance.id)
            except Exception as e:
                print("** class doesn't exist **")

    def do_show(self, arg):
        """Show the string representation of an instance"""
        args = arg.split()
        if not args:
            print("** class name missing **")
            return

        try:
            cls = eval(args[0])
        except NameError:
            print("** class doesn't exist **")
            return

        if len(args) < 2:
            print("** instance id missing **")
            return

        key = "{}.{}".format(args[0], args[1])
        all_objects = models.storage.all()
        instance = all_objects.get(key, None)

        if instance is not None:
            print(instance)
        else:
            print("** no instance found **")

    def do_destroy(self, arg):
        """Delete an instance based on the class name and id"""
        args = arg.split()
        if not args:
            print("** class name missing **")
            return

        try:
            cls = eval(args[0])
        except NameError:
            print("** class doesn't exist **")
            return

        if len(args) < 2:
            print("** instance id missing **")
            return

        key = "{}.{}".format(args[0], args[1])
        all_objects = models.storage.all()
        instance = all_objects.get(key, None)

        if instance is not None:
            del all_objects[key]
            models.storage.save()
        else:
            print("** no instance found **")

    def do_all(self, arg):
        """Print all string representations of instances"""
        args = arg.split()
        all_objects = models.storage.all()
        obj_list = []
        if not arg:
            for key, value in all_objects.items():
                obj_list.append(str(value))
        else:
            try:
                cls = eval(args[0])
                for key, value in all_objects.items():
                    if cls == type(value):
                        obj_list.append(str(value))
            except NameError:
                print("** class doesn't exist **")
                return

        print(obj_list)

    def do_update(self, arg):
        """Update an instance based on class name and id"""
        args = arg.split()
        if not args:
            print("** class name missing **")
            return

        try:
            cls = eval(args[0])
        except NameError:
            print("** class doesn't exist **")
            return

        if len(args) < 2:
            print("** instance id missing **")
            return

        key = "{}.{}".format(args[0], args[1])
        all_objects = models.storage.all()
        instance = all_objects.get(key, None)

        if instance is not None:
            if len(args) < 3:
                print("** attribute name missing **")
                return
            if len(args) < 4:
                print("** value missing **")
                return

            setattr(instance, args[2], args[3].strip('\"'))
            instance.save()
        else:
            print("** no instance found **")


if __name__ == '__main__':
    HBNBCommand().cmdloop()
