import time

class Timer():
    def __init__(self):
        self.seconds = None

    def __enter__(self):
        print("Entering")
        self.start = time.time()
        return self

    def sleep(self, seconds):
        time.sleep(seconds)
        self.seconds = seconds
        return seconds


    def __exit__(self, exc_type, exc_val, exc_tb):
        self.end = time.time()
        self.duration = self.end - self.start
        print("Exiting")
        print('Time taken: ', self.duration)



with Timer() as t:
    t.sleep(0)
    print(t.seconds)
    print("Timer started")