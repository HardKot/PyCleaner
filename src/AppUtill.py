import os

from src.Bytes import Bytes


def get_dir_size(path):
    size = 0
    for root, dirs, files in os.walk(path):
        for file in files:
            fp = os.path.join(path, file)
            size += os.path.getsize(fp)
        for dir_ in dirs:
            size += get_dir_size(os.path.join(root, dir_))
    return Bytes(size)