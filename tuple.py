<<<<<<< HEAD
#!/usr/bin/env python
str = "abc def hgi"
str = str.split(" ")
str = tuple(str)
print str
def test_tuple(tup):
    print tup[0]
    print tup[1]
    print tup[2]
test_tuple(str)
