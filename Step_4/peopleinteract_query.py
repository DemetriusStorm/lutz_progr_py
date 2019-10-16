# интерактивные запросы

import shelve

fieldnames = ('name', 'age', 'job', 'pay')
maxfield = max(len(f) for f in fieldnames)

db = shelve.open('class-shelve')

while True:
    key = input('\nKey? => ')  # key or empty stroke generate assert in input EOF

    if not key:
        break
    try:
        record = db[key]  # execute record by key and print
    except:
        print('No such key \'{}\'!'.format(key))
    else:
        for field in fieldnames:
            print(field.ljust(maxfield), '=>', getattr(record, field))
