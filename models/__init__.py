
# Import specific modules or symbols to make them accessible
from models.engine.file_storage import FileStorage
from models.base_model import BaseModel

# Create the variable storage, an instance of FileStorage
storage  = FileStorage()
# Call reload() method on this variable
storage.reload()
