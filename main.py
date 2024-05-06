#!/usr/bin/python3
"""Main module for demonstrating the storage capabilities."""

from models import storage
from models.base_model import BaseModel
from os import getenv

def demo_storage():
    """Function to demonstrate storage operations."""
    # Create a new instance of BaseModel
    new_obj = BaseModel()
    print(f"Created a new object with ID: {new_obj.id}")

    # Save the new object to storage
    storage.save()
    print("Saved the object to storage.")

    # Retrieve all objects from storage
    all_objs = storage.all()
    print(f"Retrieved {len(all_objs)} objects from storage.")

if __name__ == "__main__":
    print("Running environment:", getenv('HBNB_ENV'))
    print("Storage type:", getenv('HBNB_TYPE_STORAGE'))
    demo_storage()
