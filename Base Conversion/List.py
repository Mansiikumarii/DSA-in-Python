#Convert to list

'''
A List is a mutable (changable) , ordered collection in Python.
It can store different data types(int, float, string, list, etc.)
'''

l = [10, "Hello",3.14,True, 10, 20]

# List Assignment and Slicing

a = [5,6,7,8]
a[ : 2] = [3,4]
print(a)

a = [5,6,7,8]
a[ : 3] = a[1 : ]
print(a)

a = [ 5,6,7,8,9,10]
a[ 1 : 3] = []
print(a)

#Nested List:-
L = [[1,2,3],[4,5,6],[7,8,9]]
print(L[-1][1: ])
print(L[-1][-1])

M= L # Alias
M[0][0] = 900
print(L)

'''
Common List Methods
1. append()
2. extend()
3. insert()
4. remove()
5. pop()
6. clear()
7. index()
8. count()
9. sort()
10. reverse()

append(item)
item : Iterable / Non iterable , It takes one argument , and append element at last and return None
'''

l = [1,2]
print(l.append(3))
print(l)
print(l.append((3,4)))
print(l)
l.append({4,5})
print(l)
l.append("abc")
print(l)

'''
Extend (iterable)
Add multiple items at the end
'''
print(l.extend([4,5,6]))
print(l)

'''
Accetable iterables
list ----> [1,2,3]
Tuple ----> (1,2,3)
String ----> "abc"
Set   -----> {1,2,3}
Dictionary --> {"a" : 1 , "b" : 2}
-> keys extend hoga
'''
l = [1]
print(l.extend({10,20,30}))
print(l)

'''
insert (index item)
insert item at a specific position
'''
l=[10,20,30,30]
print(l.insert(1,99))
print(l)

l = [1,2,3]
l.insert(1,"hello")
print(l)

l = [1,2]
print(l.insert(1,(3,4)))
print(l)

l = [1,2,3]
print(l.insert(2,[100,200]))
print(l)

# remove(item)
l=[1,2,3,2,4]
print(l.remove(2))
print(l)
# Only first occurance of 2 remove

l = ["mahi", "mansi", "himani"]
print(l.remove("himani"))
print(l)

l = [1,(3,4), 5]
l.remove((3,4))
print(l)

l= [1,{"a" : 10}, 3]
l.remove({"a":10})
print(l)

l=[1,{5,6},2]
l.remove({5,6})
print(l)

'''
pop() ->
remove last element and return
'''
l = [10,20,30]
x = l.pop()
print(x,l)

'''
pop(index) ---->
remove at specific index and return 
'''
l = [10,20,30,40]
x = l.pop(2)
print(x,l)

l = [1,2,3]
# l.pop(10) # Error bcz index out of range

l = []
#l.pop() #Error bcz list empty

l = [1,2,3,4]
x = l.pop(1)
l.append(x)
print(l)

'''
pop() vs remove() :-
pop() :-
remove by index
Last element

remove() :-
remove by value
first matching value

list.clear():-
clear() remove all items from list, leaving it empty return None
'''

l = [1, "a", [10,20], {"x":13}]
print(l.clear())
print(l)

'''
len()
len(list) ->
Return total number of items in a list
'''

l1 = [ 1,2,3,4]
print(len(l1))

'''
index() :-
List index(item)  --->>
Returns the first index of the given item
If item not found --->> Value Error

Sum() :-
Returns sum of all members in a list
'''
l = [10,20,30]
print(sum(l))

'''
reverse():-
List reverse() --->
Reverse the list in place(changes original list) returns None
'''
l = [1,2,3,4]
l.reverse()
print(l)
x = l.reverse()
print(x)
print(l)

'''
Sort():-
sort the list in ascending order , modifies original list
'''
l = [40,10,30,20]
l.sort()
print(l)
# Descending order :
l.sort(reverse = True)
print(l)

'''
Sorting strings
'''
l = ["banana", "apple","cherry"]
l.sort()
print(l)

# Mixed type not allowed
l = [3,1,4]
print(l.append(5))
l.insert(1,9)
l.extend([7,8])
l.remove(4)
x = l.pop()
count_3 = l.count(3)
l.sort()
l.reverse()
print(l)

L = [1,2,3,4]
L.append([6,7])
print(L)

L= [1,2,3,4,5]
L.extend([6,7])
print(L)

'''
NOTE:-
append() and extend() method return None
'''
L = [1,2,3]
print(L.append(5))
print(L)

L = [1,2,3,5]
L = L.append(5)
print(L)

L = [1,2,3]
L.append(5)
print(L)

L = [1,2,3]
print(L.extend([5]))

'''
# List Comprehension
means creating list object based on some condition. It is very easy and compact way of creating list
objects from any iterable object(like list, tuple, dictinary, range, etc)
Syntax:-
List = [expression for item in iterable if condition] / optimal
'''