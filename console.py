#!/usr/bin/python3
"""
Console module for the command interpreter.
"""

import cmd
from models import storage
from models.user import User


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
        """Create a new instance of BaseModel."""
        if not arg:
            print("** class name missing **")
            return
        try:
            new_instance = eval(arg)()
            new_instance.save()
            print(new_instance.id)
        except Exception as e:
            print("**", e.__class__.__name__, str(e))

    def do_show(self, arg):
        """Prints the string representation of an instance."""
        args = arg.split()
        if len(args) == 0:
            print("** class name missing **")
            return
        if args[0] not in storage.classes:
            print("** class doesn't exist **")
            return
        if len(args) == 1:
            print("** instance id missing **")
            return
        key = args[0] + "." + args[1]
        objects = storage.all()
        if key in objects:
            print(objects[key])
        else:
            print("** no instance found **")

    def do_destroy(self, arg):
        """Deletes an instance based on the class name and id."""
        args = arg.split()
        if len(args) == 0:
            print("** class name missing **")
            return
        if args[0] not in storage.classes:
            print("** class doesn't exist **")
            return
        if len(args) == 1:
            print("** instance id missing **")
            return
        key = args[0] + "." + args[1]
        objects = storage.all()
        if key in objects:
            del objects[key]
            storage.save()
        else:
            print("** no instance found **")

    def do_all(self, arg):
        """Prints all string representation of all instances."""
        objects = storage.all()
        if not arg:
            print([str(obj) for obj in objects.values()])
            return
        args = arg.split()
        if args[0] not in storage.classes:
            print("** class doesn't exist **")
            return
        print([str(obj) for key, obj in objects.items()
               if args[0] == key.split('.')[0]])

    def do_update(self, arg):
        """Updates an instance based on the class name and id."""
        args = arg.split()
        if len(args) == 0:
            print("** class name missing **")
            return
        if args[0] not in storage.classes:
            print("** class doesn't exist **")
            return
        if len(args) == 1:
            print("** instance id missing **")
            return
        key = args[0] + "." + args[1]
        objects = storage.all()
        if key not in objects:
            print("** no instance found **")
            return
        if len(args) == 2:
            print("** attribute name missing **")
            return
        if len(args) == 3:
            print("** value missing **")
            return
        setattr(objects[key], args[2], args[3])
        storage.save()


if __name__ == '__main__':
    HBNBCommand().cmdloop()
