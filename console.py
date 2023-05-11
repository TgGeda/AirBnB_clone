#!/usr/bin/python3
"""
This module contains the entry point of the command interpreter
"""

import cmd


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


if __name__ == '__main__':
    HBNBCommand().cmdloop()

    
