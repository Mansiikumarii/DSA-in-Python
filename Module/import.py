'''
Import Statement in Python
The import statement in python is used to bring external module so that their functions, classes or variables can be used in current script.

Types of import in python:-
1) Importing entire module'''
import math
'''
2)Importing specific function or variable:-
You can import only specific part of module 
'''

from math import sqrt, pi
print(sqrt(49))
print(pi)

'''
3)Importing all functions(* wildcards)
'''
from math import *
print(sin (0))
print(log (10))

'''
Caution : This can lead to naming conflict

4)Importing with an alias

5) Importing a user defined module
*my_module.py
'''

# main.py
import calculator

result1 = calculator.add(10, 5)
print("Addition result:", result1)  # Output: 15

       





