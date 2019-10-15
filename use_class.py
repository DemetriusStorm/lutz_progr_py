from person_start import Person

bob = Person('Bob Smith', 42)
sue = Person('Sue Jones', 45, 40000)
people = [bob, sue]

for person in people:
    print(person.name, person.pay)

x = [(person.name, person.pay) for person in people]
print(x)

y = [person.name for person in people if person.age >= 45]
print(y)

z = [(person.age ** 2 if person.age >= 45 else person.age) for person in people]
print(z)
