import os.path
from datetime import timedelta

from src.AppDataStore import AppDataStore
from src.Singleton import Singleton
from src.WatcherDir import WatcherDir


class WatcherService(metaclass=Singleton):
    def __init__(self, data_store: AppDataStore):
        self.__data_store = data_store

    def add_dir_for_watcher(self, watcher_dir: WatcherDir):
        self.__data_store.add_watcher_dir(
            watcher_dir.get_name(),
            watcher_dir.get_path(),
            watcher_dir.get_max_period().days,
        )
        return self

    def remove_dir_for_watcher(self, watcher_dir: WatcherDir):
        self.__data_store.remove_watcher_dir(watcher_dir.get_name())
        return self

    def update_dir_for_watcher(self, watcher_dir: WatcherDir):
        dir_data = self.__data_store.get_watcher_dir_by_name(watcher_dir.get_name())
        dir__ = WatcherDir.Build()\
            .name(dir_data[1])\
            .path(os.path.normpath(dir_data[2]))\
            .max_period(timedelta(days=dir_data[3]) if dir_data is not None else None)\
            .build()
        if watcher_dir.get_path() is not None:
            dir__.set_path(watcher_dir.get_path())
        if watcher_dir.get_max_period() is not None:
            dir__.set_max_period(watcher_dir.get_max_period())
        self.__data_store.update_watcher_dir(watcher_dir.get_name(), watcher_dir.get_path(), watcher_dir.get_max_period().days)
        return self

    def get_dirs_for_watcher(self):
        return tuple(map(lambda dir_: WatcherDir(dir_[1], os.path.normpath(dir_[2]), timedelta(days=dir_[3]) if dir_ is not None else None),
                         self.__data_store.get_watcher_dirs()))