"""
Разбивает строку или текстовый файл на страницы для интерактивного просмотра
"""


def more(text, num_lines=15):
    lines = text.splitlines()  # подобно split('\n') но без '' в конце
    print(lines)
    # lines = text.split('\n')
    while lines:
        chunk = lines[:num_lines]
        lines = lines[num_lines:]
        for line in chunk:
            print(line)
        if lines and input('More?') not in ['y', 'Y']:
            break


if __name__ == '__main__':  # если запускается как сценарий
    import sys  # отобразить построчное содержимое
    more(open(sys.argv[1]).read(), 10)      # файла, указанного в командной строке

    # more(
    #     'Функция help, с которой мы только что познакомились, также не обладает достаточной гибкостью \n'
    #     'при отображении информации. Хотя она и пытается в некоторых ситуациях обеспечить постраничный вывод, \n'
    #     'тем не менее на некоторых компьютерах – из тех, на которых мне приходилось работать, – она неточно \n'
    #     'выбирает размер страницы. Кроме того, она вообще не обеспечивает постраничный просмотр в графическом \n'
    #     'интерфейсе IDLE; вместо этого предлагается использовать полосу прокрутки, что весьма неудобно на \n'
    #     'больших мониторах. Когда мне требуется получить более полный контроль над тем, как функция help \n'
    #     'будет выводить текст, я обычно использую свой собственный вспомогательный сценарий, представленный \n'
    #     'в примере 2.1. \n'
    #     'Функция help, с которой мы только что познакомились, также не обладает достаточной гибкостью \n'
    #     'при отображении информации. Хотя она и пытается в некоторых ситуациях обеспечить постраничный вывод, \n'
    #     'тем не менее на некоторых компьютерах – из тех, на которых мне приходилось работать, – она неточно \n'
    #     'выбирает размер страницы. Кроме того, она вообще не обеспечивает постраничный просмотр в графическом \n'
    #     'интерфейсе IDLE; вместо этого предлагается использовать полосу прокрутки, что весьма неудобно на \n'
    #     'больших мониторах. Когда мне требуется получить более полный контроль над тем, как функция help \n'
    #     'будет выводить текст, я обычно использую свой собственный вспомогательный сценарий, представленный \n'
    #     'в примере 2.1.', 10)
