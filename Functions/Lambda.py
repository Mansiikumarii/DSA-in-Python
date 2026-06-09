'''
Lambda function in python (Annoymous function)
A lambda function in python is a small, anonymous function using lambda keyword
'''
square = lambda x : x*x
print(square(5))

'''
Equalivalent to:-
'''
def square(x):
    return x*x
print(square(5))

#Lambda with multiple arguments
add = lambda a,b : a+b
print(add(3,5))

def fold(fn, lst):
    res = lst[0]
    for x in lst[1:]:
        res = fn(res,x)
    return res
print(fold(lambda a,b : b-a, [1,3,5,7]))

'''
Using lambda with map(), filter() and redunce()
'''
numbers = [1,2,3,4,5]
square = list(map(lambda x : x**2, numbers))
print(square)

'''
Syntax:-
map(function, itreable)
using filter() [Filters Elements Based on condition] return iterator
'''
numbers = [1,2,3,4,5,6]
even_numbers = list(filter(lambda x: x%2 == 0, numbers))
print(even_numbers)

'''
Syntax:-
filter(function, iterable)
reduce():-
reduce all elements to single value by repeatedly applying function
return single value

Syntax:-
reduce(function, iterable, initilizer) 
initilizer - optional
'''

from functools import reduce
numbers = [1,2,3,4]
result = reduce(lambda x,y : x+y, numbers)
print(result)

data = [1,2,3,4,5]
result = reduce(lambda x,y : x-2*y, data, 10)
print(result)

def r():
    if not hasattr(r,"num"):
        r.num = 7
    temp = r.num
    r.num -= 1
    return temp
r()
while r():
    print(r(), end=" ")
    r()

def outer():
    x = []
    def inner(val):
        x.append(val)
        return x
    return inner
f1 = outer()
f2 = outer()
print(f1(10))
print(f1(20))
print(f2(30))
print(f1(40))

def fun(L, i=0):
    if i>= len(L)-1:
        return 0
    if L[i] > L[i+1]:
        L[i+1], L[i] = L[i], L[i+1]
        return 1+fun(L,i+1)
    else:
        return fun(L,i+1)
data = [5,3,4,1,2]
count = 0
for _ in range(len(data)):
    count += fun(data)
print(count)

#Reverse a list
def fun(D, s1, s2):
    if s1 < s2:
        D[s1], D[s2] = D[s2], D[s1]
        fun(D, s1 + 1, s2 - 1)

D = [1, 2, 3, 4, 5]
fun(D, 0, len(D) - 1)
print(D)  # Output: [5, 4, 3, 2, 1]

def count(child_dict, i):
    if i not in child_dict.keys():
        return 1
    ans = 1
    for j in child_dict[i]:
        ans += count(child_dict,j)
    return ans
child_dict = dict()
child_dict[0] = [1,2]
child_dict[1] = [3,4,5]
print(count(child_dict,0))

