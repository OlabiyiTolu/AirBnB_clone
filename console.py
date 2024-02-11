#!/usr/bin/env python3
"""
AirBnB Console - Your Ultimate Command-Line Experience
"""

import cmd
import json
import shlex
from models import storage
from models.base_model import BaseModel
from datetime import datetime

class HBNBCommand(cmd.Cmd):
    """
    Welcome to AirBnB Console - Your Ultimate Command-Line Experience!
    """
    prompt = "\033[94m(AirBnB) \033[0m"

    def emptyline(self):
        """
        Do nothing on an empty line.
        """
        pass

    def quit(self, arg):
        """
        Exit the AirBnB Console.
        """
        print("\033[91mExiting AirBnB Console. Goodbye!\033[0m")
        return True

    def help_quit(self):
        """
        Help message for the quit command.
        """
        print("Exit the AirBnB Console.")

    def EOF(self, arg):
        """
        Exit on EOF (Ctrl-D).
        """
        print("\n\033[91mExiting AirBnB Console. Goodbye!\033[0m")
        return True

    def help_EOF(self):
        """
        Help message for the EOF command.
        """
        print("Exit on EOF (Ctrl-D)")

    def create(self, arg):
        """
        Create a new instance of BaseModel, save it (to the JSON file), and print the id.
        Usage: create <class name>
        """
        args = shlex.split(arg)
        if not args:
            print("\033[91m** Class name missing. Usage: create <class name> **\033[0m")
            return
        class_name = args[0]
        if class_name not in storage.classes:
            print("\033[91m** Class doesn't exist. **\033[0m")
            return
        new_instance = storage.classes[class_name]()
        new_instance.save()
        print("\033[92m{}\033[0m".format(new_instance.id))

    def show(self, arg):
        """
        Print the string representation of an instance based on the class name and id.
        Usage: show <class name> <id>
        """
        args = shlex.split(arg)
        if not args or len(args) < 1:
            print("\033[91m** Class name missing. Usage: show <class name> <id> **\033[0m")
            return
        class_name = args[0]
        if class_name not in storage.classes:
            print("\033[91m** Class doesn't exist. **\033[0m")
            return
        if len(args) < 2:
            print("\033[91m** Instance id missing. **\033[0m")
            return
        instance_id = args[1]
        key = "{}.{}".format(class_name, instance_id)
        all_instances = storage.all()
        if key not in all_instances:
            print("\033[91m** No instance found. **\033[0m")
            return
        print(all_instances[key])

    def destroy(self, arg):
        """
        Delete an instance based on the class name and id (save the change into the JSON file).
        Usage: destroy <class name> <id>
        """
        args = shlex.split(arg)
        if not args or len(args) < 1:
            print("\033[91m** Class name missing. Usage: destroy <class name> <id> **\033[0m")
            return
        class_name = args[0]
        if class_name not in storage.classes:
            print("\033[91m** Class doesn't exist. **\033[0m")
            return
        if len(args) < 2:
            print("\033[91m** Instance id missing. **\033[0m")
            return
        instance_id = args[1]
        key = "{}.{}".format(class_name, instance_id)
        all_instances = storage.all()
        if key not in all_instances:
            print("\033[91m** No instance found. **\033[0m")
            return
        del all_instances[key]
        storage.save()
        print("\033[92mInstance deleted successfully.\033[0m")

    def all(self, arg):
        """
        Print all string representations of instances based or not on the class name.
        Usage: all [class name]
        """
        args = shlex.split(arg)
        all_instances = storage.all()
        if not args:
            print("\033[92m{}\033[0m".format([str(all_instances[key]) for key in all_instances]))
        else:
            class_name = args[0]
            if class_name not in storage.classes:
                print("\033[91m** Class doesn't exist. **\033[0m")
                return
            print("\033[92m{}\033[0m".format([str(all_instances[key]) for key in all_instances if key.startswith(class_name)]))

    def update(self, arg):
        """
        Update an instance based on the class name and id by adding or updating an attribute
        (save the change into the JSON file).
        Usage: update <class name> <id> <attribute name> "<attribute value>"
        """
        args = shlex.split(arg)
        if not args or len(args) < 1:
            print("\033[91m** Class name missing. Usage: update <class name> <id> <attribute name> \"<attribute value>\" **\033[0m")
            return
        class_name = args[0]
        if class_name not in storage.classes:
            print("\033[91m** Class doesn't exist. **\033[0m")
            return
        if len(args) < 2:
            print("\033[91m** Instance id missing. **\033[0m")
            return
        instance_id = args[1]
        key = "{}.{}".format(class_name, instance_id)
        all_instances = storage.all()
        if key not in all_instances:
            print("\033[91m** No instance found. **\033[0m")
            return
        if len(args) < 3:
            print("\033[91m** Attribute name missing. **\033[0m")
            return
        attribute_name = args[2]
        if len(args) < 4:
            print("\033[91m** Value missing. **\033[0m")
            return
        attribute_value = args[3].strip('"')
        instance = all_instances[key]
        try:
            setattr(instance, attribute_name, eval(attribute_value))
        except (AttributeError, NameError):
            setattr(instance, attribute_name, attribute_value)
        instance.save()
        print("\033[92mAttribute updated successfully.\033[0m")

if __name__ == '__main__':
    print("\033[94mWelcome to AirBnB Console - Your Ultimate Command-Line Experience!\033[0m")
    HBNBCommand().cmdloop()
