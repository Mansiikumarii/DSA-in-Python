'''
A recusive call is passed as an argument to another recursive call. This is called nested recursion. The function calls itself again and again until it reaches the base case. The function is called with a different argument each time, which is usually a smaller value than the previous one. This process continues until the base case is reached, at which point the function returns a value and the previous calls can continue to execute. Nested recursion can be used to solve complex problems that require multiple levels of recursion.
'''

def nested(n):
    if n>100:
        return n-10
    return nested(nested(n+11))
print(nested(99))

def get(n):
    if n<1:
        return
    get(n-1)
    get(n-3)
    print(n, end=" ")
get(5)

def f(a,b):
    if a==0:
        return b
    if a%2 == 1:
        return 2*f((a-1)//2,b)
    return b+f(a-1,b)
print(f(15,10))