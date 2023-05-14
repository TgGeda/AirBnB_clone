#!/usr/bin/python3
"""This module contain the HBNB console"""

import cmd
from models.base_model import BaseModel
from models.user import User
from models.place import Place
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.review import Review
from models import storage
import models
import json


class HBNBCommand(cmd.Cmd):
    """Command line interpreter HBNB"""
    prompt = "(hbnb) "
    class_list = ["BaseModel", "User", "Place", "State\
", "City", "Amenity", "Review"]

    def do_quit(self, args):
        """Quit command to exit the console"""
        return True

    def do_EOF(self, args):
        """EOF command to exit the console"""
        return True

    def emptyline(self):
        """Perform nothing when there's no commmand passed to the console"""
        pass

    def do_create(self, args):
        """Creates a new class instance, save in JSON file and print the Id\n
        Usage: (hbnb) create <class_name>"""
        if args == "":
            print("** class name missing **")
        elif args not in HBNBCommand.class_list:
            print("** class doesn't exist **")
        else:
            a = eval(args)()
            print(a.id)
            a.save()

    def do_show(self, args):
        """Prints the string representation of an instance based
        on the class name and id"""
        sw = 0
        arg = args.split()
        if args == "":
            print("** class name missing **")
        elif arg[0] not in HBNBCommand.class_list:
            print("** class doesn't exist **")
        elif len(arg) < 2:
            print("** instance id missing **")
        else:
            in_key = (arg[0] + "." + arg[1])
            for key, obj in storage.all().items():
                if key == in_key:
                    print(obj)
                    sw = 1
            if sw == 0:
                print("** no instance found **")

    def do_destroy(self, args):
        """Deletes an instance based on the class name and id
        updating JSON file\nUsage: (hbnb) destroy <class_name> <class_id>"""
        sw = 0
        arg = args.split()
        if args == "":
            print("** class name missing **")
        elif arg[0] not in HBNBCommand.class_list:
            print("** class doesn't exist **")
        elif len(arg) < 2:
            print("** instance id missing **")
        else:
            in_key = (arg[0] + "." + arg[1])
            dict_objects = storage.all()
            for key, obj in dict_objects.items():
                if key == in_key:
                    del dict_objects[key]
                    sw = 1
                    storage.save()
                    storage.reload()
                    return
            if sw == 0:
                print("** no instance found **")

    def do_all(self, args):
        """Prints all string representation of all instances
        based or not on the class name"""
        list_ = []
        if args == "":
            for key, obj in storage.all().items():
                list_.append(str(obj))
            print(list_)
        elif args in HBNBCommand.class_list:
            for key, obj in storage.all().items():
                if args == key.split(".")[0]:
                    list_.append(str(obj))
            print(list_)
        else:
            print("** class doesn't exist **")

    def do_update(self, args):
        """Updates an instance based on the class name and id by adding or
        updating attribute, saving on JSON file"""
        arg = args.split()
        sw = 0
        if len(arg) < 1:
            print("** class name missing **")
        elif arg[0] not in HBNBCommand.class_list:
            print("** class doesn't exist **")
        elif len(arg) < 2:
            print("** instance id missing **")
        elif len(arg) < 3:
            print("** attribute name missing **")
        elif len(arg) < 4:
            print("** value missing **")
        else:
            in_key = (arg[0] + "." + arg[1])
            for key, obj in storage.all().items():
                if key == in_key:
                    idx_arg = len(arg[0]) + len(arg[1]) + len(arg[2]) + 3
                    value = args[idx_arg:]
                    if args[idx_arg] == "\"":
                        idx_arg += 1
                        value = args[idx_arg:-1]
                    if hasattr(obj, arg[2]):
                        value = type(getattr(obj, arg[2]))(args[idx_arg:])
                    setattr(obj, arg[2], value)
                    sw = 1
                    storage.save()
            if sw == 0:
                print("** no instance found **")
                return -1

    def default(self, args):
        """default method that perfom actions when no command it's given"""
        count = 0
        if len(args.split(".")) > 1:
            class_name = args.split(".")[0]
            if class_name in HBNBCommand.class_list:
                try:
                    if args.split(".")[1] == "all()":
                        self.do_all(class_name)
                    if args.split(".")[1] == "count()":
                        for key, obj in storage.all().items():
                            if key.split(".")[0] == class_name:
                                count += 1
                        print(count)
                    if args.split(".")[1].split("(")[0] == "show":
                        id_ = args.split("\"")[1].split("\"")[0]
                        self.do_show(class_name + " " + id_)
                    if args.split(".")[1].split("(")[0] == "destroy":
                        id_ = args.split("\"")[1].split("\"")[0]
                        self.do_destroy(class_name + " " + id_)
                    if args.split(".")[1].split("(")[0] == "update":
                        arg_list = args.split(".", 1)[1]
                        arg_list = arg_list.split("(")[1][:-1].split(",")
                        if "{" not in arg_list[1]:
                            id_ = arg_list[0][1:-1]
                            name = arg_list[1][2:-1]
                            value = arg_list[2][1:]
                            if value[0] == "\"":
                                value = value[1:-1]
                            self.do_update(class_name + "\
 " + id_ + " " + name + " " + value)
                        else:
                            id_ = arg_list[0][1:-1]
                            arg_dict = args.split(".")[1]
                            arg_dict = arg_dict.split("(")[1][:-1]
                            arg_dict = arg_dict.split("{")[1]
                            arg_dict = "{" + arg_dict
                            dictionary = eval(arg_dict)
                            for key, value in dictionary.items():
                                ret = self.do_update(class_name + "\
 " + id_ + " " + key + " " + str(value))
                                if ret == -1:
                                    break
                except Exception:
                    cmd.Cmd.default(self, args)
        else:
            cmd.Cmd.default(self, args)


if __name__ == "__main__":
    comand = HBNBCommand()
    comand.cmdloop()
