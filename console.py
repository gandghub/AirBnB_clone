#!/usr/bin/python3
"""
Console module for the command interpreter.
"""
import json
import cmd
from models.base_model import BaseModel
from models import storage


class HBNBCommand(cmd.Cmd):
    """Command interpreter class."""
    prompt = "(hbnb) "

    def do_EOF(self, arg):
        """Exit the program when CTRL+D is pressed."""
        print("")
        return True

    def do_quit(self, arg):
        """Quit command to exit the program."""
        return True

    def emptyline(self):
        """Do nothing on empty line."""
        pass

    def do_create(self, arg):
        """Creates a new instance of BaseModel, saves it """
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
        """Prints the string representation of an instance """
        if not arg:
            print("** class name missing **")
            return
        try:
            args = arg.split()
            class_name = args[0]
            instance_id = args[1]
            instances = storage.all()
            key = "{}.{}".format(class_name, instance_id)
            if key in instances:
                print(instances[key])
            else:
                print("** no instance found **")
        except IndexError:
            print("** instance id missing **")
        except NameError:
            print("** class doesn't exist **")

    def do_destroy(self, arg):
        """Deletes an instance based on the class name and id """
        if not arg:
            print("** class name missing **")
            return
        try:
            args = arg.split()
            class_name = args[0]
            instance_id = args[1]
            instances = storage.all()
            key = "{}.{}".format(class_name, instance_id)
            if key in instances:
                del instances[key]
                storage.save()
            else:
                print("** no instance found **")
        except IndexError:
            print("** instance id missing **")
        except NameError:
            print("** class doesn't exist **")

    def do_all(self, arg):
        """Prints all string representation of all instances based"""
        instances = storage.all()
        if arg:
            try:
                eval(arg)
                print([str(v) for k, v in instances.items() if arg in k])
            except NameError:
                print("** class doesn't exist **")
        else:
            print([str(v) for v in instances.values()])

    def do_update(self, arg):
        """Updates an instance based on the class name and id by adding"""
        if not arg:
            print("** class name missing **")
            return
        try:
            args = shlex.split(arg)
            class_name = args[0]
            instance_id = args[1]
            attribute_name = args[2]
            attribute_value = args[3]
            instances = storage.all()
            key = "{}.{}".format(class_name, instance_id)
            if key not in instances:
                print("** no instance found **")
                return
            instance = instances[key]
            setattr(instance, attribute_name, attribute_value)
            instance.save()
        except IndexError:
            print("** instance id missing **")
        except NameError:
            print("** class doesn't exist **")
        except AttributeError:
            print("** attribute name missing **")
        except ValueError:
            print("** value missing **")


if __name__ == '__main__':
    HBNBCommand().cmdloop()
