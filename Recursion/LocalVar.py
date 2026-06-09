'''
A Local variable is a variable that is defined inside a function or a block of code and only be accessed within that function or block.
- Local variables are created when the function is called.
- THey are destroyed when the function execution is completed.
'''
def my_function():
    x = 10
    print("Inside function:", x)
my_function()
#print(x) # Error because x is not defined outside the function

x = 20
def myfunc():
    print(x)
    print(x+x)
myfunc()
print(x)

'''
x = 20
def myfun():
    x = x+1
myfun()
print(x)

# Error
'''
x = 20
def myfunc():
    x = 1
    x = x+1
    print(x)
myfunc()
print(x)

x = 20
def myfun():
    print(x)
myfun()
print(x)

'''
x = 20
def myfun():
    print(x) Error : cannot access local variable 'x' where it not associated with a value
    x = 1
myfun()
print(x)'''

x = 20
def myfunc(x):
    print(x)
    x = 10
    print(x)
myfunc(x)
print(x)
