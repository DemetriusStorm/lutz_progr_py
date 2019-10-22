#!/usr/bin/python

import cgi
import html

form = cgi.FieldStorage()           # парсинг данных формы
print('Content-type: text/html\n')  # http-заголовок плюс пустая строка
print('<title>Reply Page</title>')  # html-разметка ответа
if 'user' not in form:
    print('<h1>Who are you, and WHAT ARE YOU DOING HERE?!!!</h1>')
else:
    print('<h1>Hello <i>{}</i></h1>'.format(html.escape(form['user'].value)))
