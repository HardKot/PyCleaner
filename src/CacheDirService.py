from src.AppDataStore import AppDataStore
from src.CacheDir import CacheDir
from src.Singleton import Singleton


class CacheDirService(metaclass=Singleton):
    def __init__(self, data_store: AppDataStore):
        self.__data_store = data_store


    def add_cache_dir(self, cache_dir: CacheDir):
        self.__data_store.add_cache_dir(cache_dir.name, cache_dir.path, cache_dir.command_clear)
        return self

    def remove_cache_dir(self, cache_dir: CacheDir):
        self.__data_store.remove_cache_dir(cache_dir.name)
        return self

    def get_cache_dir_list(self):
        return tuple(map(lambda x: CacheDir(x[1], x[2], x[3]), self.__data_store.get_cache_dir()))
