import os
import re
from datetime import timedelta

from src.AppConfig import AppConfig
from src.CacheDir import CacheDir
from src.CacheDirService import CacheDirService
from src.Singleton import Singleton
from src.WatcherDir import WatcherDir
from src.WatcherService import WatcherService


class AppController(metaclass=Singleton):
    def __init__(self, app_config: AppConfig, cache_dir_service: CacheDirService, watcher_dir_service: WatcherService):
        self.__app_config = app_config
        self.__cache_dir_service = cache_dir_service
        self.__watcher_dir_service = watcher_dir_service

    def clear_cache(self):
        cache_dirs = self.__cache_dir_service.get_cache_dir_list()
        for cache_dir in cache_dirs:
            if self.__app_config.get_max_size() < cache_dir.get_size():
                cache_dir.clear()
        return self

    def add_cache_dir(self, name, path, command_clear = None):
        self.__cache_dir_service.add_cache_dir(
            CacheDir.Build()
                .name(name)
                .path(path)
                .command_clear(command_clear)
                .build()
        )
        return self

    def delete_cache_dir(self, name):
        self.__cache_dir_service.remove_cache_dir(name)
        return self


    def clear_watcher(self):
        watcher_dirs = self.__watcher_dir_service.get_dirs_for_watcher()
        for watcher_dir in watcher_dirs:
            watcher_dir.clear()
        return self

    def add_watcher(self, name, path, max_period):
        timedelta__ = self.__get_timedelta(max_period)

        self.__watcher_dir_service.add_dir_for_watcher(
            WatcherDir.Build()
                .name(name)
                .path(os.path.join(os.path.expanduser("~"), path))
                .max_period(timedelta__)
                .build())
        return self

    def delete_watcher(self, name):
        self.__watcher_dir_service.remove_dir_for_watcher(name)
        return self

    def update_watcher(self, name, max_period, path):
        timedelta__ = self.__get_timedelta(max_period)

        self.__watcher_dir_service.update_dir_for_watcher(
            WatcherDir.Build()
                .name(name)
                .path(os.path.join(os.path.expanduser("~"), path))
                .max_period(timedelta__)
                .build()
        )
        return self

    def __get_timedelta(self, value):
        week_match = re.match(r'\d*(W|w)', value)
        week = week_match.group().replace("W", "").replace("w", "") if week_match is not None else 0

        day_match = re.match(r'\d*(D|d)', value)
        day = day_match.group().replace("D", "").replace("d", "") if day_match is not None else 0

        if len(week) > 0:
            timedelta__ = timedelta(weeks=int(week))
        elif len(day) > 0:
            timedelta__ = timedelta(days=int(day))
        else:
            timedelta__ = timedelta(days=0)

        return timedelta__