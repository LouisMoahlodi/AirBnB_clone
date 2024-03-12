#!/usr/bin/python3
# Import specific modules or symbols to make them accessible
from .base_model import BaseModel
from models.engine.file_storage import FileStorage

# Create the variable storage, an instance of FileStorage
storage  = FileStorage()
# Call reload() method on this variable
storage.reload()
