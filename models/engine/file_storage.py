import os
import json
from models.base_model import BaseModel

class FileStorage:
    __file_path = "file.json"
    __objects = {}

    def all(self):
        return FileStorage.__objects

    def new(self, obj):
        object_class_name = obj.__class__.__name__
        key = "{}.{}".format(object_class_name, obj.id)
        FileStorage.__objects[key] = obj

    def save(self):
        all_objects = FileStorage.__objects
        object_dict = {}
        for obj in all_objects.keys():
            object_dict[obj] = all_objects[obj].to_dict()
        with open(FileStorage.__file_path, "w", encoding = "utf-8") as file:
            json.dump(object_dict, file)

    def reload(self):
        if os.path.isfile(FileStorage.__file_path):
            with open(FileStorage.__file_path, "r", encoding = "utf-8") as file:
                try:
                    object_dict = json.load(file)
                    for key, value in object_dict.items():
                        class_name, object_id = key.split(".")
                        class_nm = eval(class_name)
                        instance = class_nm(**values)
                        FileStorage.__objects[key] = instance
                except Exception:
                    pass
