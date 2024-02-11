#!/usr/bin/env python3
"""
A command interpreter program for managing AirBnB objects.
"""

import cmd
import json
import shlex
from models.base_model import BaseModel

class HBNBCommand(cmd.Cmd):
    """
    Custom command interpreter class for AirBnB objects.
    """
    prompt = "(hbnb) "
    valid_classes = ["BaseModel"]

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

    def do_create(self, arg):
        """
        Creates a new instance of BaseModel, saves it (to the JSON file) and prints the id.
        Usage: create <class name>
        """
        args = shlex.split(arg)
        if len(args) == 0:
            print("** class name missing **")
            return
        class_name = args[0]
        if class_name not in self.valid_classes:
            print("** class doesn't exist **")
            return
        new_instance = BaseModel()
        new_instance.save()
        print(new_instance.id)

    def do_show(self, arg):
        """
        Prints the string representation of an instance based on the class name and id.
        Usage: show <class name> <id>
        """
        args = shlex.split(arg)
        if len(args) == 0:
            print("** class name missing **")
            return
        class_name = args[0]
        if class_name not in self.valid_classes:
            print("** class doesn't exist **")
            return
        if len(args) < 2:
            print("** instance id missing **")
            return
        instance_id = args[1]
        instance = self.find_instance(class_name, instance_id)
        if instance:
            print(instance)
        else:
            print("** no instance found **")

    def do_destroy(self, arg):
        """
        Deletes an instance based on the class name and id (save the change into the JSON file).
        Usage: destroy <class name> <id>
        """
        args = shlex.split(arg)
        if len(args) == 0:
            print("** class name missing **")
            return
        class_name = args[0]
        if class_name not in self.valid_classes:
            print("** class doesn't exist **")
            return
        if len(args) < 2:
            print("** instance id missing **")
            return
        instance_id = args[1]
        instance = self.find_instance(class_name, instance_id)
        if instance:
            del instance
            print("Instance deleted")
        else:
            print("** no instance found **")

    def do_all(self, arg):
        """
        Prints all string representation of all instances based or not on the class name.
        Usage: all [<class name>]
        """
        args = shlex.split(arg)
        if len(args) == 0:
            print(self.all_string_representation())
        else:
            class_name = args[0]
            if class_name not in self.valid_classes:
                print("** class doesn't exist **")
                return
            print(self.all_string_representation(class_name))

    def do_update(self, arg):
        """
        Updates an instance based on the class name and id by adding or updating attribute.
        Usage: update <class name> <id> <attribute name> "<attribute value>"
        """
        args = shlex.split(arg)
        if len(args) == 0:
            print("** class name missing **")
            return
        class_name = args[0]
        if class_name not in self.valid_classes:
            print("** class doesn't exist **")
            return
        if len(args) < 2:
            print("** instance id missing **")
            return
        instance_id = args[1]
        instance = self.find_instance(class_name, instance_id)
        if not instance:
            print("** no instance found **")
            return
        if len(args) < 4:
            print("** attribute name missing **")
            return
        attribute_name = args[2]
        attribute_value = args[3]
        setattr(instance, attribute_name, attribute_value)
        instance.save()

    def find_instance(self, class_name, instance_id):
        """
        Finds an instance by class name and id.
        """
        try:
            with open("file.json", "r") as file:
                all_instances = json.load(file)
                key = "{}.{}".format(class_name, instance_id)
                return all_instances[key]
        except FileNotFoundError:
            return None
        except KeyError:
            return None

    def all_string_representation(self, class_name=None):
        """
        Returns a list of string representations of all instances.
        """
        result = []
        try:
            with open("file.json", "r") as file:
                all_instances = json.load(file)
                if class_name:
                    for key, value in all_instances.items():
                        if class_name in key:
                            result.append(str(value))
                else:
                    for value in all_instances.values():
                        result.append(str(value))
        except FileNotFoundError:
            pass
        return result

if __name__ == '__main__':
    HBNBCommand().cmdloop()
