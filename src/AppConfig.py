from datetime import timedelta

from src.Singleton import Singleton
from src.AppDataStore import AppDataStore
from src.Bytes import Bytes


class AppConfig(metaclass=Singleton):
    MAX_SIZE = "maxSize"
    PERIOD_CLEAR = "periodClear"

    def __init__(self, app_data_store: AppDataStore):
        self.__app_data_store = app_data_store
        configs = self.__app_data_store.get_config()

        self.__max_size = None
        self.__period_clear = None

        for config in configs:
            if config[0] == AppConfig.PERIOD_CLEAR:
                days = int(config[1])
                self.__period_clear = timedelta(days=days)
            elif config[0] == AppConfig.MAX_SIZE:
                self.__max_size = Bytes(int(config[1]))


    def get_max_size(self):
        return self.__max_size

    def get_max_size_human(self):
        return self.__max_size.get_human_size()


    def set_max_size(self, max_size: Bytes):
        self.__max_size = max_size
        self.__app_data_store.update_config(AppConfig.MAX_SIZE, max_size.bytes)


    def get_period_clear(self):
        if self.__period_clear is None:
            return timedelta()
        return self.__period_clear

    def set_period_clear(self, period: timedelta):
        self.__period_clear = period

        self.__app_data_store.update_config(AppConfig.PERIOD_CLEAR, f"{self.__period_clear.days}")


