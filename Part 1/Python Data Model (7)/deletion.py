import sys
import time


class Buffer:
    def __init__(self, maxlength=50):
        self._data = b""
        self.maxlength = maxlength

    def write(self, msg):
        if len(self._data) < self.maxlength:
            self._data += msg[:self.maxlength - len(self._data)]

    def flush(self):
        if self._data:
            sys.stdout.write(self._data.decode("utf-8"))
            self._data = b""

    def __del__(self):
        print("Deleting...")
        self.flush()


b1 = Buffer()
b1.write(b"Mike is hosting!")
b2 = Buffer()
b1.other = b2
del b1
while True:
    print("stuff")
    time.sleep(1)