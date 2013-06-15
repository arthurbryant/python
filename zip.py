#!/usr/bin/env python
ages = [1, 2, 3]
names = ['arthur', 'wendy', 'tom']
for i in range(len(ages)):
    print names[i], "is", ages[i], "years old."
z = zip(ages, names)
print z
for (age, name) in z:
    print name, "is", age, "years old."

