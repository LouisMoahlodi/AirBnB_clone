#!/usr/bin/python3
"""
Module for the HBNB console.
"""
import cmd
import json
from models.base_model import BaseModel
from models import storage


class HBNBCommand(cmd.Cmd):
    """
    HBNBCommand class for the command interpreter.
    """

    prompt = '(hbnb) '

    def do_quit(self, arg):
        """
        Quit command to exit the program.
        """
        return True

    def do_EOF(self, arg):
        """
        EOF command to exit the program.
        """
        print()
        return True

    def emptyline(self):
        """
        Do nothing when an empty line is entered.
        """
        pass

    def do_create(self, arg):
        """
        Creates a new instance of BaseModel, saves it (to the JSON file)
        and prints the id.
        Usage: create <class name>
        """
        if not arg:
            print("** class name missing **")
            return

        try:
            new_instance = eval(arg)()
            new_instance.save()
            print(new_instance.id)
        except NameError:
            print("** class doesn't exist **")

    def do_show(self, arg):
        """
        Prints the string representation of an instance based on the
        class name and id.
        Usage: show <class name> <id>
        """
        if not arg:
            print("** class name missing **")
            return

        args = arg.split()
        if len(args) == 1:
            print("** instance id missing **")
            return

        try:
            obj = storage.all()[args[0] + "." + args[1]]
            print(obj)
        except KeyError:
            print("** no instance found **")

    def do_destroy(self, arg):
        """
        Deletes an instance based on the class name and id (save the
        change into the JSON file).
        Usage: destroy <class name> <id>
        """
        if not arg:
            print("** class name missing **")
            return

        args = arg.split()
        if len(args) == 1:
            print("** instance id missing **")
            return

        try:
            del storage.all()[args[0] + "." + args[1]]
            storage.save()
        except KeyError:
            print("** no instance found **")

    def do_all(self, arg):
        """
        Prints all string representation of all instances based or not on
        the class name.
        Usage: all [<class name>]
        """
        objs = storage.all()
        if not arg:
            print([str(obj) for obj in objs.values()])
        else:
            try:
                class_name = eval(arg).__name__
                print([str(obj) for key, obj in objs.items() if key.startswith(class_name)])
            except NameError:
                print("** class doesn't exist **")

    def do_update(self, arg):
        """
        Updates an instance based on the class name and id by adding or
        updating attribute (save the change into the JSON file).
        Usage: update <class name> <id> <attribute name> "<attribute value>"
        """
        if not arg:
            print("** class name missing **")
            return

        args = arg.split()
        if len(args) == 1:
            print("** instance id missing **")
            return

        try:
            obj = storage.all()[args[0] + "." + args[1]]
        except KeyError:
            print("** no instance found **")
            return

        if len(args) == 2:
            print("** attribute name missing **")
            return

        if len(args) == 3:
            print("** value missing **")
            return

        key = args[0] + "." + args[1]
        attribute_name = args[2]
        attribute_value = args[3]

        if hasattr(obj, attribute_name):
            attribute_value = type(getattr(obj, attribute_name))(attribute_value)
            setattr(obj, attribute_name, attribute_value)
            storage.save()
        else:
            print("** attribute doesn't exist **")

if __name__ == '__main__':
    HBNBCommand().cmdloop()
