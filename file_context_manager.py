class FileContextManager():
    def __init__(self, filename, mode):
        self.filename = filename
        self.mode = mode

    def __enter__(self):
        self.file = open(self.filename, self.mode)
        return self.file

    def __exit__(self, exc_type, exc_value, exc_tb):
        self.file.close()


with FileContextManager("testfile.txt", "r") as file:
    content = file.read()
    print(content)

with FileContextManager("testfile.txt", "a") as file:
    new_content = file.write("\n Add a new line")