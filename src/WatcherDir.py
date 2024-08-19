from src.AbstractDir import AbstractDir
import os

from src.WatcherContent import WatcherContent


class WatcherDir(AbstractDir):
    def __init__(self, name, path, max_period):
        super().__init__(path)
        self.__name = name
        self.__max_period = max_period
        self.__contents = None

    def get_name(self):
        return self.__name

    def set_name(self, name):
        self.__name = name

    def get_max_period(self):
        return self.__max_period

    def set_max_period(self, max_period):
        self.__max_period = max_period

    def get_contents(self):
        if self.__contents is None:
            self.refresh_content()
        return tuple(self.__contents)

    def refresh_content(self):
        contents = []
        for root, dirs, files in os.walk(self.get_path()):
            for file in files:
                contents.append(
                    WatcherContent(os.path.join(root, file), self)
                )
            for dir_ in dirs:
                contents.append(
                    WatcherContent(os.path.join(root, dir_), self)
                )
        self.__contents = contents
        return self


    def clear(self):
        for content in self.get_contents():
            if content.is_old():
                content.clear()
        return self

    class Build:
        def __init__(self):
            self.__name = None
            self.__path = None
            self.__max_period = None

        def name(self, value):
            self.__name = value
            return self

        def path(self, value):
            self.__path = value
            return self

        def max_period(self, value):
            self.__max_period = value
            return self

        def build(self):
            return WatcherDir(self.__name, self.__path, self.__max_period)