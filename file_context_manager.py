class FileContextManager():
    def __init__(self, filename, mode):
        self.filename = filename
        self.mode = mode

    def __enter__(self):
        try:
            self.file = open(self.filename, self.mode)
            return self.file

        except FileNotFoundError:
            print("File not found")
            return None

    def __exit__(self, exc_type, exc_value, exc_tb):
        try:
            self.file.close()
        except AttributeError:
            pass
        if exc_type:
            print(f"An error occurred: {exc_value}")
            return True
        return None


#Testing with a non existent file:
with FileContextManager("testf.txt", "r") as file:
    if file:
        content = file.read()
        print(content)

with FileContextManager("testfile.txt", "a") as file:
    new_content = file.write("\n Add a new line")