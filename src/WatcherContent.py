import os
import shutil
from datetime import datetime

from src import AppUtill

class WatcherContent:
    def __init__(self, path, watcher_dir):
        self.path = path
        self.watcher_dir = watcher_dir
        self.__size = None

    def get_size(self):
        if self.__size is None:
            self.refresh_size()
        return self.__size

    def refresh_size(self):
        if os.path.isdir(self.path):
            self.__size = AppUtill.get_dir_size(self.path)
        elif os.path.isfile(self.path):
            self.__size = os.path.getsize(self.path)
        return self

    def get_created_at(self):
        mtime = os.path.getmtime(self.path)
        return datetime.fromtimestamp(mtime)

    def is_old(self):
        if self.watcher_dir.get_max_period().days == 0:
            return False
        return datetime.now() - self.get_created_at() > self.watcher_dir.get_max_period()

    def clear(self):
        if not os.path.exists(self.path):
            return self
        if os.path.isdir(self.path):
            shutil.rmtree(self.path)
        elif os.path.isfile(self.path):
            os.remove(self.path)
        return self