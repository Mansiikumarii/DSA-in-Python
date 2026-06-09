'''
A global variable is a variable that is defined outside of any function or block and is accessible throughout the entire program, including functions and blocks. Global variables can be accessed and modified from any part of the program, making them useful for storing values that need to be shared across multiple functions or blocks. However, it is important to use global variables with caution, as they can lead to unintended consequences if not managed properly. It is generally recommended to minimize the use of global variables and instead pass values as arguments to functions or return values from functions when possible. 
- Global variable are created when the program starts and remain in the memory until the program ends.
- They can be accessed an modified inside function, but to modify them , you need to use global keyword inside the function.

Modifying Global Varibale Inside Functions:
If you want to modify a global variable inside function, you need to descibe it global inside the function. This tells Python that you want to use the global variable instead of creating a new local variable with the same name. Here is an example:
'''
x = 20
def modify_global():
    global x
    x = 50
print(modify_global()) # None
print(x) # 50

'''
"globL" keyword serves two purposes:
1. modify existing global functions
'''
x = 300
def num_func():
    global x
    x = 5
num_func()
print(x) # 5

'''
2) There is no existing global variable, we need to define global varible inside the function and then we can use it outside the function.
'''
def func():
    global x
    x = 5
    print("inside x: ", x)
func()
print("outside x: ", x)

a = 2
b = 3
def mul():
    global a
    a = 10
    b = 20
    print(a*b)
mul()
def add():
    print(a+b)
add()

a = 3
b = 3
def mul():
    global a,b
    a = 10
    b = 20
    print(a*b)
mul()
def  add():
    print(a+b)
add()

a = 2
b = 3
def mul():
    global a,b,c
    a = 10
    b = 20
    c = a*b
    print(c)
mul()
def add():
    print(a+b+c)
add()

x = 20
def myfunc():
    global x
    x = x+1
myfunc()
print(x)
