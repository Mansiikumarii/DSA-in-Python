'''
Outer(enclosing)

nonlocal is defined in an enclosing (outer) function
'''

def outer():
    x= 50
    def inner():
        nonlocal x # refer outer enclosing function variable
        x = 25
        print("Inner x: ",x)
    inner()
    print("Outer x",x)
outer()

def outer():
    x = 1
    def inner():
        x = 2
        def innermost():
            nonlocal x
            x = 3
            return x
        return innermost()
    return inner()+x
result = outer()
print(result)
