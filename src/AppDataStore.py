import sqlite3
import os.path

from src.Singleton import Singleton


def get_config_dir():
    path = os.path.join(os.path.expanduser("~"), ".config", "pyCacheController")
    if not os.path.exists(path):
        os.makedirs(path)
    return path

def init_database(cursor):
    try:
        cursor.execute("SELECT * FROM Migrations")
    except:
        cursor.executescript('''
            CREATE TABLE Config (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                key TEXT NOT NULL,
                value TEXT NOT NULL
            );

            CREATE TABLE Migrations (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                name TEXT NOT NULL
            );
            
            CREATE TABLE CacheDir (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                name TEXT NOT NULL,
                path TEXT NOT NULL,
                command_clear TEXT
            );
            
            CREATE TABLE WatcherDir (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                name TEXT NOT NULL,
                path TEXT NOT NULL,
                max_period INTEGER NOT NULL
            );

            INSERT INTO Migrations (name) VALUES ('init');
            
        ''')

class AppDataStore(metaclass=Singleton):
    def __init__(self):
        database_path = os.path.join(get_config_dir(), "config.db")
        self.__connect = sqlite3.connect(database_path)
        self.__cursor = self.__connect.cursor()
        self.__migration__()

    def get_config(self):
        return self.__cursor.execute("SELECT * FROM Config").fetchall()

    def update_config(self, name, value):
        self.__cursor.execute("UPDATE Config SET value = ? WHERE name = ?", (value, name))
        self.__connect.commit()
        return self

    def get_cache_dir(self):
        return self.__cursor.execute("SELECT * FROM CacheDir").fetchall()

    def add_cache_dir(self, name, path, command_clear = None):
        if command_clear is None:
            self.__cursor.execute("INSERT INTO CacheDir (name, path) VALUES (?, ?)", (name, path))
        else:
            self.__cursor.execute("INSERT INTO CacheDir (name, path, command_clear) VALUES (?, ?, ?)", (name, path, command_clear))
        self.__connect.commit()
        return self

    def remove_cache_dir(self, name):
        self.__cursor.execute("DELETE FROM CacheDir WHERE name = ?", (name,))
        self.__connect.commit()
        return self

    def add_watcher_dir(self, name, path, max_period = 0):
        self.__cursor.execute("INSERT INTO WatcherDir(name, path, max_period) VALUES (?, ?, ?)",
                              (name, path, max_period))
        self.__connect.commit()
        return self

    def remove_watcher_dir(self, name):
        self.__cursor.execute("DELETE FROM WatcherDir WHERE name = ?", (name,))
        self.__connect.commit()
        return self

    def update_watcher_dir(self, name, path, max_period = 0):
        self.__cursor.execute("UPDATE WatcherDir SET max_period = ?, path = ? WHERE name = ?",
                              (max_period, path, name))
        self.__connect.commit()
        return self

    def get_watcher_dirs(self):
        return self.__cursor.execute("SELECT * FROM WatcherDir").fetchall()

    def get_watcher_dir_by_name(self, name):
        return self.__cursor.execute("SELECT * FROM WatcherDir WHERE name = ?", (name,)).fetchone()

    def __migration__(self):
        init_database(self.__cursor)
        return self