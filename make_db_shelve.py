from initdata import bob, sue
import shelve

db = shelve.open('people-pickle')
db['bob'] = bob
db['sue'] = sue
db.close()
