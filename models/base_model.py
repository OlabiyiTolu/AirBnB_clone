#!/usr/bin/env python3
"""
This class defines a base model framework for other classes,
providing common attributes and methods for basic data management.
"""

import uuid
from datetime import datetime
import models

class BaseModel:
    """
    Base class for all model classes.

    Attributes:
        id (str): A unique identifier assigned using UUID.
        created_at (datetime): Date and time of object creation.
        updated_at (datetime): Date and time of last object update.

    Methods:
        save(self): Updates the `updated_at` attribute to the current datetime.
        to_dict(self): Returns a dictionary representation of the object.
        __str__(self): Returns a string representation of the object.
    """

    def __init__(self, *args, **kwargs):
        """
        Initializes a new Base Model instance.

        Assigns unique IDs and timestamps upon creation.
        """
        TIME_FORMAT = "%Y-%m-%dT%H:%M:%S.%f"
        if kwargs:
            for key, value in kwargs.items():
                if key == "__class__":
                    continue  # Ignore "__class__" key
                elif key in ["created_at", "updated_at"]:
                    try:
                        setattr(self, key, datetime.strptime(value, TIME_FORMAT))
                    except ValueError:
                        raise ValueError(f"Invalid timestamp format for {key}: {value}")
                else:
                    setattr(self, key, value)

            if "id" not in kwargs:
                self.id = str(uuid.uuid4())
        else:
            self.id = str(uuid.uuid4())
            
            self.created_at = datetime.now()
            self.updated_at = datetime.now()
        models.storage.new(self)

    def save(self):
        """
        Updates the `updated_at` attribute to reflect object changes.

        Used to indicate when an object's information has been modified.
        """
        self.updated_at = datetime.now()
        models.storage.save()

    def to_dict(self):
        """
        Creates a dictionary representation of the object's attributes.

        Includes class name, unique ID, and datetime attributes in ISO format.
        Useful for serialization and data exchange.

        Returns:
            dict: A dictionary containing object attributes.
        """
        self_dict = self.__dict__.copy()
        self_dict["__class__"] = self.__class__.__name__
        self_dict["created_at"] = self.created_at.isoformat()
        self_dict["updated_at"] = self.updated_at.isoformat()
        return self_dict

    def __str__(self):
        """
        Provides a clear and informative string representation of the object.

        Includes class name, unique ID, and a dictionary of instance attributes.

        Returns:
            str: A formatted string representation of the object.
        """
        return f"[{self.__class__.__name__}] ({self.id}) {self.__dict__}"
