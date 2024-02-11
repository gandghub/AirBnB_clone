#!/usr/bin/python3
import os.path
import json
from models.base_model import BaseModel
from models.user import User


class FileStorage:
    """
    Serializes instances to a JSON file and deserializes JSON file to instances
    """

    __file_path = "file.json"
    __objects = {}

    def all(self):
        """Returns the dictionary __objects"""
        return self.__objects

    def new(self, obj):
        """Sets in __objects the obj with key <obj class name>.id"""
        if obj:
            key = "{}.{}".format(obj.__class__.__name__, obj.id)
            self.__objects[key] = obj

    def save(self):
        """Serializes __objects to the JSON file (path: __file_path)"""
        my_dict = {}
        for key, val in self.__objects.items():
            my_dict[key] = val.to_dict()

        with open(self.__file_path, "w") as my_file:
            json.dump(my_dict, my_file)

    def reload(self):
        """Deserializes/loads the JSON file to __objects"""
        if not os.path.isfile(self.__file_path):
            return

        my_dict = {
            "BaseModel": BaseModel,
            "User": User,
        }

        with open(self.__file_path, "r") as file_path:
            objects = json.load(file_path)
            self.__objects = {}
            for key, value in objects.items():
                name = key.split(".")[0]
                self.__objects[key] = my_dict[name](**value)
