#Immutable list (locked list)

t = 10,20,30,40
print(t)
print(type(t))

'''
t = (10,20,"Hello", True,10)
Immutable (locked) can't change
t[0] = 20 # Error bcz tuple is not mutable

NOTE:-
We have to take special care about single valued tuple compulosary. The value should end with comma,
otherwise it is not treated as tuple.
'''
t = 10
print(t)
print(type(t))

#Few valid tuples
t=()
t = 10,20,30,40
t=10,
t=(10,)

#Modification in Tuples
t = (10,20,30.5, "Hello",[40,50,60])
# t[0] = 100 error bcz tuple is mutable
t[4][0] = 100
print(t)

'''
Sorted():-
To sort elements based on default natural sorting order
->Numbers =>Ascending order
->String => Dictionary order (Lexicographical order)
'''
t= (10,20,30,20,40)
t1 = sorted(t)
print(t1)
print(t)

'''
We can sort according to reverse or default natural sorting order 
'''

t1 = sorted(t1, reverse=True)
print(t1)

'''
NOTE:-
sort():-
function sort the existing list
sorted():-
function create new list and sort the new list
'''

t1 = (10,40,30,20,50)
t2 = sorted(t1)
t3 = sorted(t1, reverse=True)
print(t1)
print(t2)
print(t3)
print(type(t1))

'''
Tuple Comprehension:-
- Tuple comprehension is not supported by python
- Here we are not getting tuple object we are getting generator object
'''

t=(x**2 for x in range(1,6))
print(type(t)) 
for x in t:
    print(x)