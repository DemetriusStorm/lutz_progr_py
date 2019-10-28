"""
Разбивает строку или текстовый файл на страницы для интерактивного просмотра
"""


def more(text, num_lines=15):
    lines = text.splitlines()               # подобно split('\n') но без '' в конце
    while lines:
        chunk = lines[:num_lines]
        lines = lines[num_lines:]
        for line in chunk:
            print(line)
        if lines and input('More?') not in ['y', 'Y']:
            break


if __name__ == '__main__':                  # если запускается как сценарий
    import sys                              # отобразить построчное содержимое
    more(open(sys.argv[1]).read(), 5)      # файла, указанного в командной строке
