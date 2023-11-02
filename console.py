#!/usr/bin/python3
"""create console"""
import cmd


class HBNBCommand(cmd.Cmd):
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


if __name__ == '__main__':
    HBNBCommand().cmdloop()
