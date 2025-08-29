# --------------------------- Context Managers --------------------------- #

# Creating custom context manager

class Open_File():
    def __init__(self, filename, mode):
        self.filename = filename
        self.mode = mode

    def __enter__(self):
        self.file = open(self.filename, self.mode)
        return self.file

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.file.close()


with Open_File('testfile.txt', 'w') as file:
    print("file is closed" if file.closed is True else "file is open")
    file.write("Testing...")

print("Done")
print("file is closed" if file.closed is True else "file is open")
