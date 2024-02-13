import os
import json
from models.base_model import BaseModel

class FileStorage:
    __file_path = "file.json"
    __objects = {}

    def all(self):
        """
        Returns the dictionary of all objects.
        """
        return FileStorage.__objects

    def new(self, obj):
        """
        Adds a new object to the storage.
        """
        object_class_name = obj.__class__.__name__
        key = "{}.{}".format(object_class_name, obj.id)
        FileStorage.__objects[key] = obj

    def save(self):
        """
        Saves the objects to the JSON file.
        """
        all_objects = FileStorage.__objects
        object_dict = {key: obj.to_dict() for key, obj in all_objects.items()}
        with open(FileStorage.__file_path, "w", encoding="utf-8") as file:
            json.dump(object_dict, file)

    def reload(self):
        """
        Reloads objects from the JSON file.
        """
        if os.path.isfile(FileStorage.__file_path):
            with open(FileStorage.__file_path, "r", encoding="utf-8") as file:
                try:
                    object_dict = json.load(file)
                    for key, values in object_dict.items():
                        class_name, object_id = key.split(".")
                        class_obj = eval(class_name)
                        instance = class_obj(**values)
                        FileStorage.__objects[key] = instance
                except Exception as e:
                    print(f"Error reloading objects: {e}")