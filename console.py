#!/usr/bin/python3
"""
This module contains the entry point of the command interpreter
"""

import cmd
from models.base_model import BaseModel
from models import storage


class HBNBCommand(cmd.Cmd):
    """
    Class for the command interpreter
    """
    prompt = "(hbnb) "

    def do_quit(self, arg):
        """
        Quit command to exit the program
        """
        return True

    def do_EOF(self, arg):
        """
        Exit the program using EOF
        """
        return True

    def emptyline(self):
        """
        Do nothing on empty line
        """
        pass

    def help_help(self):
        """
        Help documentation for help command
        """
        print("List available commands with 'help' or detailed help with 'help cmd'.")

    def help_quit(self):
        """
        Help documentation for quit command
        """
        print("Quit command to exit the program.")

    def help_EOF(self):
        """
        Help documentation for EOF command
        """
        print("Exit the program using EOF.")

    def do_create(self, arg):
        """
        Creates a new instance of BaseModel, saves it (to the JSON file) and prints the id.
        """
        args = arg.split()
        if len(args) == 0:
            print("** class name missing **")
            return
        try:
            new_instance = eval(args[0])()
            new_instance.save()
            print(new_instance.id)
        except NameError:
            print("** class doesn't exist **")

    def do_show(self, arg):
        """
        Prints the string representation of an instance based on the class name and id.
        """
        args = arg.split()
        if len(args) == 0:
            print("** class name missing **")
            return
        try:
            class_name = args[0]
            obj_id = args[1]
        except IndexError:
            print("** instance id missing **")
            return
        try:
            obj = storage.all()[class_name + "." + obj_id]
            print(obj)
        except KeyError:
            print("** no instance found **")

    def do_destroy(self, arg):
        """
        Deletes an instance based on the class name and id (save the change into the JSON file).
        """
        args = arg.split()
        if len(args) == 0:
            print("** class name missing **")
            return
        try:
            class_name = args[0]
            obj_id = args[1]
        except IndexError:
            print("** instance id missing **")
            return
        try:
            obj = storage.all()[class_name + "." + obj_id]
            del storage.all()[class_name + "." + obj_id]
            storage.save()
        except KeyError:
            print("** no instance found **")

    def do_all(self, arg):
        """
        Prints all string representation of all instances based or not on the class name.
        """
        args = arg.split()
        objects = storage.all()
        if len(args) == 0:
            print([str(obj) for obj in objects.values()])
        else:
            try:
                class_name = args[0]
                print([str(obj) for obj in objects.values() if type(obj).__name__ == class_name])
            except NameError:
                print("** class doesn't exist **")

    def do_update(self, arg):
        """
        Updates an instance based on the class name and id by adding or updating attribute (save the change into the JSON file).
        """
        args = arg.split()
        if len(args) == 0:
            print("** class name missing **")
            return
        try:
            class_name = args[0]
            obj_id = args[1]
        except IndexError:
            print("** instance id missing **")
            return
        try:
            obj = storage.all()[class_name + "." + obj_id]
        except KeyError:
            print("** no instance found **")
            return
        if len(args) == 2:
            print("** attribute name missing **")
            return
        if len(args) == 3:
            print("** value missing **")
            return
        if len(args) > 4:
            print("** too many arguments **")
            return
        try:
            attr_name = args[2]
            attr_value = args[3]
            setattr(obj, attr_name, type(getattr(obj, attr_name))(attr_value))
            obj.save()
        except AttributeError:
            setattr(obj, attr_name, attr_value)
            obj.save()


if __name__ == '__main__':
    HBNBCommand().cmdloop()
