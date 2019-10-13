bob = ['Bob Smith', 42, 30000, 'software']
sue = ['Sue Jones', 45, 25000, 'hardware']

#bob[0].split()[-1]
#bob[0].split()[::-1]

people = [bob, sue]
print("Iteration rezult.")
for person in people:
  person[2] *= 9.5
  print("Second Name: {}, money: {}".format(person[0].split()[-1], person[2]))

# выбрать все оклады
years = [person[1] for person in people]
print(years)

pays = [person[2] for person in people]
print(pays)

#####################################################################################
# Функция map
bob = ['Bob Smith', 42, 30000, 'software']
sue = ['Sue Jones', 45, 25000, 'hardware']

print('=======================================================================')
#years = map((lambda x: x[1]), people)
print("Years:", *map((lambda x: x[1]), people))
#pays = map((lambda x: x[2]), people)
print("Pays:", *map((lambda x: x[2]), people))
print("Summa:", sum(person[2] for person in people))

people.append(['Tom', 50, 13698, None])
list(people)

# Обращение к полям по именам
NAME, AGE, PAY = range(3)
bob = ['Bob Smith', 42, 10000]
#bob[NAME]
#PAY, bob[PAY]

bob = [['name', 'Bob Smith'], ['age', 42], ['pay', 10000]]
sue = [['name', 'Sue Jones'], ['age', 45], ['pay', 20000]]
people = [bob, sue]

for person in people:
  print(person[0][1], person[2][1])

for person in people:
  for name, value in person:
    if name == 'name':
      print("Name:", value)

def field(record, label):
  for fname, fvalue in record:
    if fname == label:
      return fvalue

field(bob, 'name')
field(sue, 'pay')

for rec in people:
  print(field(rec, 'age'))
#####################################################################################
# Словари
print('=======================================================================')
bob = {'name': 'Bob Smith', 'age': 42, 'pay': 30000, 'job': 'dev'}
sue = {'name': 'Sue Jones', 'age': 45, 'pay': 40000, 'job': 'hdw'}
#bob['name'], sue['pay']

bob = dict(name='Bob Smith', age=42, pay=30000, job='dev')
print(bob)
sue = dict(name='Sue Jones', age=45, pay=34500, job='hdw')
print(sue)

# Запонение словаря поле за полем
sue = {}
sue['name'] = 'Sue Jones'
sue['age'] = 45
sue['pay'] = 34500
sue['job'] = 'hdw'
print(sue)

# Объединение двух списов
names = ['name', 'age', 'pay', 'job']
values = ['Sue Jones', 43, 34678, 'hdw']
list(zip(names, values))

sue = dict(zip(names, values))
print(sue)

# Создание словаря из последовательности ключей
fields = ('name', 'age', 'pay', 'job')
record = dict.fromkeys(fields, '?')
print(record)

# Списки словарей
people = [bob, sue]

for person in people:
  print(person['name'], person['pay'], sep=', ')

for person in people:
  if 'Sue' in person['name']:
    print(person['pay'])

print([person['name'] for person in people])
print(list(map((lambda x: x['name']), people)))
print(sum(person['pay'] for person in people))

print([rec['name'] for rec in people if rec['age'] >= 40])
print([(rec['age'] ** 2 if rec['age'] >= 40 else rec['age']) for rec in people])

G = (rec['name'] for rec in people if rec ['age'] >= 40)
next(G)

G = ((rec['age'] ** 2 if rec['age'] >= 40 else rec['age']) for rec in people)
G.__next__()

# А так как словари являются обычными объектами, к этим записям
# можно также обращаться с использованием привычного синтаксиса:

for person in people:
  print(person['name'].split()[-1])  # Second name
  person['pay'] *= 1.10

for person in people:
  print(person['pay'])
#####################################################################################
# Вложенные структуры
print('=======================================================================')
bob2 = {'name': {'first': 'Bob', 'last': 'Smith'},
        'age': 42,
        'job': ['software', 'writing'],
        'pay': (40000, 50000)
        }
print(bob2['name'])
#bob2['name']['last']
#bob2['pay'][1]
bob2['job'].append('janitor')
print(bob2['job'])

# Словари словарей

bob = dict(name='Bob Smith', age=42, pay=30000, job='dev')
sue = dict(name='Sue Jones', age=40, pay=40000, job='hdw')

db = {}
db['bob'] = bob
db['sue'] = sue
#db['bob']['name']
print(db)

#####################################################################################
print('=======================================================================')
# Форматириованный вывод с помощью pprint
bob = dict(name='Bob Smith', age=42, pay=30000, job='dev')
sue = dict(name='Sue Jones', age=40, pay=40000, job='hdw')
db = {}
#db['bob'] = bob
#db['sue'] = sue
#db['bob']['name']

import pprint
pprint.pprint(db)

for key in db:
  print(key, '=>', db[key]['name'], '=>', db[key]['pay'])

for key in db:
  print(db[key]['name'].split()[-1])
  db[key]['pay'] *= 1.10

for record in db.values():
  print(record['pay'])

x = [db[key]['name'] for key in db]
x = [rec['name'] for rec in db.values()]

# Добавление записи
db['tom'] = dict(name='Tom', age=35, job=None, pay=0)
#db['tom']
#db['tom']['name']
list(db.keys())

ab = [rec['name'] for rec in db.values() if rec['age'] >= 40]

#####################################################################################
