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