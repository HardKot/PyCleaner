class Bytes:
    def __init__(self, bytes_):
        self.bytes = bytes_

    def get_human_size(self):
        if self.bytes < 1024:
            return f"{self.bytes} byte"
        if self.bytes < 1024 ** 2:
            return f"{self.bytes // Bytes.KB} KB"
        if self.bytes < 1024 ** 3:
            return f"{self.bytes // Bytes.MB} MB"
        return f"{self.bytes // Bytes.GB} GB"

    def __eq__(self, other):
        if isinstance(other, Bytes):
            return self.bytes == other.bytes
        return False

    def __ne__(self, other):
        if isinstance(other, Bytes):
            return self.bytes != other.bytes
        return False

    def __lt__(self, other):
        if isinstance(other, Bytes):
            return self.bytes < other.bytes
        return False

    def __le__(self, other):
        if isinstance(other, Bytes):
            return self.bytes <= other.bytes
        return False

    def __gt__(self, other):
        if isinstance(other, Bytes):
            return self.bytes > other.bytes
        return False

    def __ge__(self, other):
        if isinstance(other, Bytes):
            return self.bytes >= other.bytes
        return False


    KB = 1024 ** 2
    MB = 1024 ** 3
    GB = 1024 ** 3
