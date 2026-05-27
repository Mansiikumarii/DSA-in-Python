'''
A for loop is used to iterate over a sequence / collection and execute a block of code for each item in the sequence. The syntax of a for loop is:
for item in sequence:
    code block

Here sequence mean range(), string, list, tuple, set, dictionary, etc. The code block will be executed for each item in the sequence.

Syntax:
for x in sequence:
    body
else:
    body

NOTE:-
else is optional , inside loop execution if break statement is not executed then else part will be executed otherwise else part will be skipped.

range():-
It generates a sequence of numbers starting from 0 (by default) and increments by 1 (by default) and ends at a specified number. The syntax of range() is:
range(stop)

range(arg1, arg2, arg3)
arg1: Starting number of the sequence (inclusive). Default is 0.
arg2: Stopping number of the sequence (exclusive).
arg3: Step size (optional). Default is 1. Can't be zero.
All must be integers (positive, negative, or zero). If a non-integer is passed, it will raise a TypeError.
'''

for x in range(5,20,3):
    print(x)

'''
Case 2:-
range(arg1, arg2)
arg1: Starting number of the sequence (inclusive). Default is 0.
arg2: Stopping number of the sequence (exclusive).
step size is 1 by default.

Case 3:-
range(arg1)
arg1: Stopping number of the sequence (exclusive).
Starting number is 0 by default and step size is 1 by default.
'''

for x in range(2):
    print(x)

'''
for x in range(2,6,0):
    print(x)
Output:-
ValueError: range() arg 3 must not be zero

'''

for x in range(10,5, -1):
    print(x)

for x in range(10, 5, -2):
    print(x)

for x in range(-10, -1, 1):
    print(x)

for x in range(2,6,-1):
    print(x)

for x in range(5,0,1):
    print(x)

for x in range(5,5,1):
    print(x)