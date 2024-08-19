import os
import shutil

from src import AppUtill


class AbstractDir:
    def __init__(self, path):
        self.__size = None
        self.__path = path

    def get_human_size(self):
        size = self.get_size()
        return size.get_human_size()


    def get_path(self):
        return self.__path

    def set_path(self, path):
        self.__path = path


    def clear(self):
        if os.path.exists(self.__path) and os.path.isdir(self.__path):
            shutil.rmtree(self.__path)
        return self

    def refresh_size(self):
        self.__size = AppUtill.get_dir_size(self.__path)
        return self

    def get_size(self):
        if self.__size is None:
            self.refresh_size()
        return self.__size
