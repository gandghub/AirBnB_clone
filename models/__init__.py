#!/usr/bin/python3
"""Creates a singleton  file storage for the Storage engine.
"""

from models.engine.file_storage import FileStorage

storage = FileStorage()
storage.reload()
