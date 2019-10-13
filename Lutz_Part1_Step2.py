# Сохранение записей на длительное время
# Текстовые файлы

# инициализировать данные для последующего сохранения в файлах
# записи

bob = {'name': 'Bob Smith', 'age': 42, 'pay': 30000, 'job': 'dev'}
sue = {'name': 'Sue Jones', 'age': 45, 'pay': 40000, 'job': 'hdw'}
tom = {'name': 'Tom Bradly', 'age': 50, 'pay': 0, 'job': None}

# data base

db = {'bob': bob, 'sue': sue, 'tom': tom}

if __name__ == '__main__':  # если запускается как сценарий
    for key in db:
        print(key, '=>', db[key])

#########################################################################################

"""
Сохраняет в файл базу данных, находящуюся в оперативной памяти, используя
собственный формат записи; предполагается, что в данных отсутствуют строки
‘endrec.’, ‘enddb.’ и ‘=>’; предполагается, что база данных является словарем
словарей; внимание: применение функции eval может быть опасным – она
выполняет строки как программный код; с помощью функции eval() можно также
реализовать сохранение словарей-записей целиком; кроме того, вместо вызова
print(key,file=dbfile) можно использовать вызов dbfile.write(key + ‘\n’);
"""

dbfilename = 'people-file'
ENDDB = 'enddb.'
ENDREC = 'endrec.'
RECSEP = '=>'


def store_database(db, dbfilename=dbfilename):
    """Save data base to file"""
    dbfile = open(dbfilename, 'w')
    for key in db:
        print(key, file=dbfile)
        for name, value in db[key].items():
            print(name + RECSEP + repr(value), file=dbfile)
        print(ENDREC, file=dbfile)
    print(ENDDB, file=dbfile)
    dbfile.close()


def load_database(dbfilename=dbfilename):
    """Restore data, reconstruction data base"""
    dbfile = open(dbfilename)
    import sys
    sys.stdin = dbfile
    db = {}
    key = input()
    while key != ENDDB:
        rec = {}
        field = input()
        while field != ENDREC:
            name, value = field.split(RECSEP)
            rec[name] = eval(value)
            field = input()
        db[key] = rec
        key = input()
    return db


if __name__ == '__main__':
    from initdata import db
    store_database(db)

#########################################################################################
"""выполняет загрузку базы данных из файла"""

from make_db_file import load_database

db = load_database()
for key in db:
    print(key, '=>\n', db[key])
print(db['sue']['name'])
#########################################################################################
"""загружает базу данных, вносит в нее изменения и сохраняет ее обратно в файл."""

from make_db_file import load_database, store_database

db = load_database()
db['sue']['pay'] *= 1.10
db['tom']['name'] = 'Tom Tom'

store_database(db)