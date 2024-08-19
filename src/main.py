import argparse

from src.DIContainer import DIContainer


def main():
    di_container = DIContainer()

    parser = argparse.ArgumentParser(
        prog = 'PyCleaner',
        description = 'Python program for cleaning files',
    )

    parser.add_argument('type')
    parser.add_argument("action")
    parser.add_argument('-n', '--name')
    parser.add_argument('-p', '--path')
    parser.add_argument('-c', '--command')
    parser.add_argument('--period')

    args = parser.parse_args()
    type, action = args.type, args.action

    controller = di_container.app_controller()

    if type == 'cache':
        if action == 'clear':
            controller.clear_cache()
        elif action == 'add':
            name, path, command = args.name, args.path, args.command
            controller.add_cache_dir(name, path, command)
        elif action == 'remove':
            name = args.name
            controller.delete_cache_dir(name)
    elif type == 'dir':
        if action == 'clear':
            controller.clear_watcher()
        elif action == 'add':
            name, path, period = args.name, args.path, args.period
            controller.add_watcher(name, path, period)
        elif action == 'remove':
            name = args.name
            controller.delete_watcher(name)
        elif action == 'update':
            name, path, period = args.name, args.path, args.period
            controller.update_watcher(name, period, path)

if __name__ == '__main__':
    main()