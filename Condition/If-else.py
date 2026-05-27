'''
If condition is true, then action 1 will be executed, otherwise action 2 will be executed.
Syntax:
if condition:
    Action 1
else:   
    Action 2
'''

num = int(input("Enter a number: "))
if num % 2 == 0:
    print(num, "is an even number.")
else:
    print(num, "is not an even number.")