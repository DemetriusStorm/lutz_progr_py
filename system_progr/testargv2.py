"""
собирает параметры командной строки в словарь для дальнейшей обработки
"""


def get_options(argv):
    opts = {}
    while argv:
        if argv[0][0] == '-':           # поиск пар "-name value"
            opts[argv[0]] = argv[1]     # ключами словарей будут имена параметров
            argv = argv[2:]
        else:
            argv = argv[1]
    return opts


if __name__ == '__main__':
    from sys import argv                # пример клиентского программного кода
    my_args = get_options(argv)
    if '-i' in my_args:
        print(my_args['-i'])
    print(my_args)
