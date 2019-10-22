"""
Реализует веб-интерфейс для просмотра и изменения экземпляров классов
в хранилище; хранилище находится на сервере (или на том же компьютере,
если используется имя localhost)
"""

# cgi.test() выведет поля ввода
import cgi, html, shelve, sys, os

# файлы хранилища находятся в текущем каталоге
shelve_name = 'class-shelve'
field_names = ('name', 'age', 'job', 'pay')

form = cgi.FieldStorage()             # Парсинг данных формы
print('Content-type: text/html\n')    # заголовок + пустая строка для ответа
sys.path.insert(0, os.getcwd())

# Главный шаблон разметки html
reply_html = """
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>People Input Form</title>
</head>
<body>
<form method="post" action="peoplecgi.py">
    <table>
        <tr><th>key<td><input type="text" name="key" value="%(key)s">
        $ROWS$
    </table>
    <p>
    <input type="submit" value="Fetch" name="action">
    <input type="submit" value="Updated" name="action">
</form>
</body>
</html>
"""

# вставить разметку html с данными в позицию $ROWS$
row_html = '<tr><th>%s<td><input type="text" name=%s value="%%(%s)s">\n'
rows_html = ''

for fieldname in field_names:
    rows_html += (row_html % ((fieldname,) * 3))

reply_html = reply_html.replace('$ROWS$', rows_html)


def html_size(adict):
    new = adict.copy()          # значения могут содержать &, >
    for field in field_names:   # и другие спец. символы, отображаемые
        value = new[field]      # особым образом; их необходимо экранировать
        new[field] = html.escape(repr(value))
    return new


def fetch_record(db, form):
    try:
        key = form['key'].value
        record = db[key]
        fields = record.__dict__    # для заполнения строки ответа
        fields['key'] = key         # использовать словарь атрибутов
    except:
        fields = dict.fromkeys(field_names, '?')
        fields['key'] = 'Missing or invalid key!'
    return fields


def update_record(db, form):

















