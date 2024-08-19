import os
import shutil
import subprocess

from src.AbstractDir import AbstractDir


class CacheDir(AbstractDir):
    def __init__(self, name, path, command_clear = None):
        super().__init__(path)
        self.name = name
        self.command_clear = command_clear

    def clear(self):
        if os.path.exists(self.path) and os.path.isdir(self.path):
            if self.command_clear is None:
                shutil.rmtree(self.path)
            else:
                subprocess.call(self.command_clear)
        return self

    class Build:
        def __init__(self):
            self.__name = None
            self.__path = None
            self.__command_clear = None

        def name(self, value):
            self.__name = value
            return self

        def path(self, value):
            self.__path = value
            return self

        def command_clear(self, value):
            self.__command_clear = value
            return self

        def build(self):
            return CacheDir(self.__name, self.__path, self.__command_clear)