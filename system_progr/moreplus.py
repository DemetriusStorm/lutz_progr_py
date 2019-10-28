"""
обеспечивает постраничный вывод в stdout содержимого строки, файла или потока;
если запускается как самостоятельный сценарий, обеспечивает постраничный вывод
содержимого потока stdin или файла, имя которого указывается в виде аргумента
командной строки; когда входные данные поступают через поток stdin, исключается
возможность использовать его для получения ответов пользователя --вместо этого
можно использовать платформозависимые инструменты или графический интерфейс;
"""

import sys


def getreply():
    """
    читает клавишу, нажатую пользователем,
    даже если stdin перенаправлен в файл или канал
    :return:
    """

    if sys.stdin.isatty():  # если stdin связан с консолью, читать ответ из stdin
        return input('Type \'y\' or \'Y\' to continue, or other to exit>>')
    else:
        if sys.platform[:3] == 'win':   # если stdin был перенаправлен,
            import msvcrt               # его нельзя использовать для чтения
            msvcrt.putch(b'?')          # ответа пользователя
            key = msvcrt.getche()       # использовать иснтрумент консоли
            msvcrt.putch(b'\n')         # getche(), которая не выводит символ
            return key                  # для нажатия клавиши
        else:
            assert False, 'Platform not supported'
            # For LINUX: open('/dev/tty').readline()[:-1]


def more(text, numlines=10):
    """
    реализует постраничный вывод содержимого строки в stdout
    :param text:
    :param numlines:
    :return:
    """
    lines = text.splitlines()
    while lines:
        chunk = lines[:numlines]
        lines = lines[numlines:]
        for line in chunk:
            print(line)
        if lines and getreply() not in [b'y', 'Y']:
            break


if __name__ == '__main__':              # если выполняется, а не импортируется
    if len(sys.argv) == 1:              # если нет аргументов командной строки
        more(sys.stdin.read())          # вывести содержиме stdin
    else:
        more(open(sys.argv[1]).read())  # иначе вывести содержимое файла
