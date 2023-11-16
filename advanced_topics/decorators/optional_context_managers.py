class FileManager:
    def __init__(self, filename):
        self.filename = filename

    def __enter__(self):
        self.file = open(self.filename, 'r')
        return self.file

    def __exit__(self, exc_type, exc_value, traceback):
        self.file.close()


# Usage:
with FileManager('example.txt') as file:
    content = file.read()
    # File is automatically closed upon exiting the block
