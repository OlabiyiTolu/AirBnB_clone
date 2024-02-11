#!/usr/bin/env python3
"""
A program called console.py that contains the entry point of the command interpreter.
"""

import cmd

class HBNBCommand(cmd.Cmd):
    """
    Custom command interpreter class.
    """
    prompt = "(hbnb) "

    def emptyline(self):
        """
        Do nothing on empty line.
        """
        pass

    def do_quit(self, arg):
        """
        Quit command to exit the program.
        """
        return True

    def help_quit(self):
        """
        Help message for the quit command.
        """
        print("Quit command to exit the program")

    def do_EOF(self, arg):
        """
        Exit on EOF (Ctrl-D).
        """
        print("")
        return True

    def help_EOF(self):
        """
        Help message for the EOF command.
        """
        print("Exit on EOF (Ctrl-D)")

if __name__ == '__main__':
    HBNBCommand().cmdloop()
