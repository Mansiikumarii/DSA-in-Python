'''
A function in python is a bloock of reusable code that is used to perform a specific task. It helps to break our program into smaller and modular chunks, making it more organized and easier to manage. Functions can take inputs (called parameters) and can return outputs (called return values). They are defined using the 'def' keyword followed by the function name and parentheses.
Example :
1) 234.8962 * 842.382
2) 65928.628 * 926.382
3) f(x) = 2^x
4) g(x) = sin(x)
5) print("Good Afternoon")

'''

def wish():
    print("Good Afternoon")
for i in range(100):
    wish()

'''
Why use functions?
Avoid repeation of code - If we have a block of code that we need to use multiple times, we can define it as a function and call it whenever needed, instead of writing the same code again and again.
NOTE:-

1) The purpose of function is code reusability. It allows us to write a block of code once and use it multiple times throughout our program, which can save time and effort.
2) The purpose of loop is code repetition. It allows us to execute a block of code multiple times based on a condition, which can help us to perform repetitive tasks without having to write the same code multiple times.
3) The purpose of module is function reutilization. It allows us to organize our code into separate files and reuse functions across different programs, which can help us to keep our code organized and maintainable.

Function:-
If a group of statements is repeadly required then it is not recommended to write sepeately. Instead we can define a function and call it whenever required. This is called function in python.

Build in function:-
Input/Output --------> input(), print()
Type conversion -----> int(), float(), str(), list(), tuple(), set(), dict()
Math           ------> abs(), round(), pow(), max(), min(), sum()
String         ------> len(), upper(), lower(), split(), join(), replace(),ord(), chr()
List & Sequence  ------> len(), max(), min(), sum(), sorted(), reversed(), enumerate()
Sorting / Filtering  ------> sorted(), filter(), map(), reduce()
File Handling  ------> open(), read(), write(), close()
Advanced Functions  ------> lambda(), map(), filter(), reduce(), zip(), enumerate(), eval(), exec()

User-defined function:-
The function  which is developed by programmer explicitly to buisness logic is called user defined function. It is defined using the 'def' keyword followed by the function name and parentheses. The code block within every function starts with a colon (:) and is indented.
There are two parts of a function:
1) Function definition: It is the process of creating a function by specifying its name, parameters (if any), and the block of code that defines what the function does.
2) Function call: It is the process of executing a function by using its name followed by parentheses. If the function has parameters, we can pass arguments to it within the parentheses.
Syntax of function definition:
def function_name(parameters):
    # code block
    return value

Function name: The name of the function should be descriptive and should follow the naming conventions of Python. It should start with a letter or an underscore and can be followed by letters, digits, or underscores.
parameters: Parameters are the inputs to a function. They are specified within the parentheses in the function definition. A function can have zero or more parameters, and they can be of any data type.
return: (optional) The function can return a value using the 'return' statement. If a function does not have a return statement, it will return 'None' by default.

function calling:-
var function_name(arguments)

Returning multiple values from a function:-
- In other languages like C, C++ and Java function can return at most one value.
- But in Python , a function can return any values, including multiple values as a tuple. This allows us to return multiple pieces of information from a function in a convenient way.

'''

def sum_sub(a,b):
    sum = a+b
    sub = a-b
    return sum, sub
x,y = sum_sub(200,100)
print("The sum is:", x)
print("The sub is:", y)

def mystry_fun(x,y):
    if x == 0:
        return y
    if x % 3 == 2:
        return 3 * mystry_fun((x-2)//3, y)
    return y + mystry_fun(x-1, y)
print(mystry_fun(17,5))

p = 1
q = 10
count = 0
def func(node):
    global p,q,count
    if node not in d:
        return
    for child in d[node]:
        if child%4 == 0:
            p+= child
            continue
        q -= 2
        if(p+q) % 6 == 0:
            count += 1
            break
        count += 1
        func(child)
    else:
        q += p
d = {0: [2,3,4], 2:[5,6], 3:[7,8]}
func(0)
print(p+q+count)

def func(s, choosen= " " ):
    if len(s) == 0:
        print(choosen)
    else:
        for i in range (len(s)):
            func(s[:i] + s[i+1 :], choosen + s[i])
func("ABC")

