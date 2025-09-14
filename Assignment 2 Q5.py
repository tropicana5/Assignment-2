class FileHandler:
    """Abstract base class for file handlers."""


    def read(self):
        """Read data from a file."""
        pass


    def write(self, data):
        """Write data to a file."""
        pass


# Concrete class for text files
class TextFileHandler(FileHandler):
    def __init__(self, filename):
        self.filename = filename

    def read(self):
        with open(self.filename, 'r') as f:
            return f.read()

    def write(self, data):
        with open(self.filename, 'w') as f:
            f.write(data)


# Concrete class for binary files
class BinaryFileHandler(FileHandler):
    def __init__(self, filename):
        self.filename = filename

    def read(self):
        with open(self.filename, 'rb') as f:
            return f.read()

    def write(self, data):
        with open(self.filename, 'wb') as f:
            f.write(data)

