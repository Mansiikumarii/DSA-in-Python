'''
Parameters(Function Defination Time)
'''

def add(a,b):
    return a+b
'''
a and b are parameters local scope , always variable repetition not allowed

Arguments(Function call Time)
'''
add(10,20) # Arguments constant, variable, expression
'''
Here, 10 and 20 are arguments repetition allowed
NOTE:
Parameter ---> function definition time

Parameter:-
Parameters are variable listed in a function definition

Arguments:-
Actual value passed in function

Types of Parameters/Argumnets :-
- Positional Argumenta
- Keyword Parameters
- Default Parameters
- varaible 
- Length positional parameters

Positional Parameters / Arguments
Values are assigned based on position
'''

def sub(a,b):
    print(a-b)

'''
Keyword Parameters/ Arguments
Arguments are passed using parameter names
'''
def sub(a,b):
    print(a-b)
sub(b = 5, a = 10)

def show(a,b):
    print(a,b)
show(1, b=2)
# show(a=1, 2) Error
show(1,2)
#show(1)  TypeError: show() missing 1 required positional argument: 'b'
#show() TypeError: show() missing 2 required positional arguments: 'a' and 'b'

'''
NOTE:-
First we pass positional arguments, then keyword arguments
# Default Parameters/ Arguments
Parameters with default value
'''
def greet(name= "Guest"):
    print("Hello", name)
greet()
greet("Prince")

def show(a,b=1):
    print(a,b)
show(2,3)
show(a = 1, b= 2)
show(4)

'''
NOTE:-
First define non-default arguments and then default argumets
Default arguments are evaluated once, at function definition time
'''
x = 10
def f(a=x):
    print(a)
x = 20
f()
print(x)

def fun(a,b = 5):
    print(b)
    b = 10
    print(b)
fun(1)
fun(4)

'''
Problematic mutable default argument
'''
def add_item(lst=[]):
    lst.append(1)
    print(lst)
add_item()
add_item()
add_item()

'''
Safe handling using none
'''
def add_items_safe(lst = None):
    if lst is None:
        lst = []
    lst.append(1)
    print(lst)
add_items_safe()
add_items_safe()
add_items_safe()

def f(lst = None):
    if lst is None:
        lst = []
    lst.append(1)
    print(lst)
f()
f()
f([0])
f()

def func(x, lst=[]):
    lst.append(x)
    return lst
print(func(1))
print(func(2))
print(func(3,[]))

def update(x,y=[]):
    y.append(x)
    return y
a = update(1)
b = update(2)
c = update(3,[])

def func(a,b):
    a.append(5)
    b = b+ [5]
    return a,b
x = [1,2]
y = [1,2]
func(x,y)
print(x,y)

def show(*a):
    print(a)
show(10,20,30)
show(10,20)
show()
show(1,2,3,4,5,6)
'''
*a can accept 0-n positional arguments and all arguments recieved in tuples
'''

def add(*numbers):
    total = 0
    for num in numbers:
        total += num
    return(total)
print(add(2,3))
print(add(2,3,5))
print(add(2,3,5,7))
print(add(2,3,5,7,8,9))

# Variable length keyword only
def show(**a):
    print(a)
show(i=10, j=20)
show(roll = 1011, name = "Gunjan", age = 23)
'''
**a can accepts an keyword arguments and all arguments recieved in dictionary

Position only:-
'''
def show(a,b,/):
    print(a,b)
show(1,2)
#show(a=1, b=2) TypeError: show() got some positional-only arguments passed as keyword arguments: 'a, b'
'''
All parameters before / becomes positioned only i.e accepts only positioned arguments

#Keywords only
'''
def show(*,a,b):
    print(a,b)
# show(1,2) TypeError: show() takes 0 positional arguments but 2 were given
show(a = 1, b=2)

#Positional or keywords
def show(a,b):
    print(a,b)
show(2,3)
show(a = 1, b=2)

def foo(a=0, b=0, c=0, d=0):
    print(a,b,c,d)
foo()
foo(1)
foo(1,2,3,4)
foo(1,2,d=4,c=3)
foo(1,d=4, c=3)
foo(d=4,c=3)

#Valid/ Invalid
def func(a,b, /,c, *,d):
    print(a,b,c,d)
func(1,2,3,d=4)
func(1,2,c=3, d=4)
# func(a=1, b=2, c=3, d=4) TypeError: func() got some positional-only arguments passed as keyword arguments: 'a, b'
#func(1,2,3,4) TypeError: func() takes 3 positional arguments but 4 were given
'''
def fun(a,b,/,c,*,d,e):
a,b : Positional
d,e : keyword(normal positional or keyword)

Completer order:-
positionl --> / --> normal --> * --> keyword only --> **kwargs
'''

def f(a,b,/,c,*,d,**kwargs):
    print(f"a={a}, b={b}, c={c}, d={d}, kwargs={kwargs}")
f(1,2,3,d=4,e=5,f=6,name="Alice")

'''
* vs *args
'''
def f(*,x,y): #no positional argument allowed
    print(x,y)

def g(*args,x,y):
    print(args,x,y) #Positional allowed

def f(a,b,/,c,*, d):
    pass
f(1,2,3,d=4)
f(1,2,c=3,d=4)

def f(*,x,y=5):
    pass
f(x=10)

def f(x,y=10,/,*,z=20):
    return x+y+z
print(f(5,z=15))
print(f(5))

'''
Summary table:-
positional ---> def f(a,b) : Match by order
default ------> def f(a,b=5) : Has a default value
keyword ------> f(a=1, b=2) Passed by name
variable positional ----> def f(*args) collects extra positional elements
variable keywords ------> def f(**kwargs)
'''
