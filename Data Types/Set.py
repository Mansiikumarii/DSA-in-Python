#unordered 
#no indexing(no slicing)
#mutable
# If we write empty set like {}, it will be considered as empty dictionary. To create an empty set, we need to use set() function.

empty_set = set()
print(type(empty_set))

#unique / distinct values
s={4,2,6,1,3,2,4,5}
print(s)

'''
1) Set is a collection of unique values
2) Set does not store duplicate values
3) Set does not maintain order of values
4) Set does not support indexing and slicing
5) Set is iterable
6) Set is mutable
7) It can store only immutable values
8) We can represent set elements within curly braces with a comma seperator 

S= {10,20,30.5, "Hello",(40,50),[60,70,80]}
not allowed in set bcz set is a collection of immutable values

NOTE:-
while creating empty set we have to take special care
-> cumplusory we should create set() function
-> S= {} => it is treated as dictionary but not empty set
'''


S= {}
print(S)
print(type(S))

S = set()
print(S)
print(type(S))

S= set("bharat")
print(S)

S= set(range(-5,5))
print(S) # Prints in same order due to hashing

'''
Important function of set:-
-add(x) : Add items to set, here x is immutable object
'''

S = {10,20,30}
S.add(40)
print(S)

S={1,2,3}
# S.add(4,5) TypeError: set.add() takes exactly one argument (2 given)
# S.add([4,5]) error bcz list is mutable

'''
Update(x,y,z) :-
x,y,z = Iterable
multiple sequence allowed to add multiple items to set arguments are not the individual elements and
these are iterable object like list, range etc. All elements present in the iterable objects will be
added to the set
'''

S = {10,20,30}
l = [40,50,60,10]
S.update(l, range(5))
print(S)

S = {10,20,36}
l = {40,40,50,50,10,20,70}
S.update(l,range(5), range(80,90))
print(S)


'''
3. Remove():-
Removes an element (may raise Error)
'''
S = {1,2,3}
S.remove(2)
print(S)
# S.remove(4) error
# 5. Clear():-To remove all elements from set

S = {10,20,30}
S.clear()
print(S)

'''
Mathamatical Operation
1.Union():-
x.union(y) or x|y => we can use this function present in both sets
NOTE:-
1. union will eliminate duplicate elements
2. + operator not allowed on sets

2.Intersection():-

3. Differences():-
x.difference(y) or x-y returns the elements present in x but not y

Symmentic difference():- XOR
x.symmentric_difference(y) or x^y => Return elements
'''

S1 = {1,2}
S2 = {2,3}
print(S1.intersection(S2))
print(S1.difference_update(S2))
S1.symmetric_difference_update(S2)
print(S1)
print({1,2}.issubset({1,2}))
print({1,2,3}.issuperset({2}))
print({1,2}.isdisjoint({3,4}))
print(2 in ({1,2,3}))
print(len({1,2,3}))
print(S.add((1,2)))
print(S)

S= {1,2,3}
print(S.intersection_update([2,3,4]))

S= set()
# S.add([1,2]) cannot use 'list' as a set element (unhashable type: 'list') bcz it is mutable data type

S={1,2}
t = {3,4}
print(S.isdisjoint(t))

S= {1,2,3}
print(S.symmetric_difference_update({2,3,4}))

def fun(S1, S2):
    if not S1 or not S2: #is S1 and S2 empty
        return set()
    element = S1.pop()
    if element in S2:
        return {element} | fun(S1, S2)
    else:
        return fun(S1, S2)
print(fun({2,3,4,5,6},{5,6,7,8,9}))


