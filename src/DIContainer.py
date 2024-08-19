from src.AppConfig import AppConfig
from src.AppController import AppController
from src.AppDataStore import AppDataStore
from src.CacheDirService import CacheDirService
from src.WatcherService import WatcherService


class DIContainer:
    def __init__(self):
        self.__app_data_store_component = None
        self.__app_config_component = None
        self.__watcher_service_component = None
        self.__cache_dir_service_component = None
        self.__app_controller = None

    def app_data_store_component(self):
        if self.__app_data_store_component is None:
            self.__app_data_store_component = AppDataStore()
        return self.__app_data_store_component

    def app_config_component(self):
        if self.__app_config_component is None:
            self.__app_config_component = AppConfig(self.app_data_store_component())
        return self.__app_config_component

    def watcher_service_component(self):
        if self.__watcher_service_component is None:
            self.__watcher_service_component = WatcherService(self.app_data_store_component())
        return self.__watcher_service_component

    def cache_dir_service_component(self):
        if self.__cache_dir_service_component is None:
            self.__cache_dir_service_component = CacheDirService(self.app_data_store_component())
        return self.__cache_dir_service_component

    def app_controller(self):
        if self.__app_controller is None:
            self.__app_controller = AppController(
                self.app_data_store_component(),
                self.cache_dir_service_component(),
                self.watcher_service_component()
            )
        return self.__app_controller