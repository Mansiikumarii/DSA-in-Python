'''
Immutable version of set
Set -> Mutable
frozenset -> Immutable

Syntax:-
frozenset(Iterable) 
'''

fs = frozenset([5,2,4,6,1,3,2,4,5])
print(fs)

# fs.add(10) AttributeError: 'frozenset' object has no attribute 'add'
# fs.remove(2) AttributeError: 'frozenset' object has no attribute 'remove'

fs = frozenset("Hello")
print(fs)

d = {1:'a', 2:'b', 3:'c'}
fs = frozenset(d)
print(fs)

a = frozenset([1,2,3])
b = frozenset([3,4,5])
print(a | b)
print(a & b)
print(a-b)
print(a^b)
print(2 in a)