'''
current function
variable is defined inside function
'''
x = 100
def outer():
    global x
    x = 50
    def inner():
        global x
        x = 25
        print("Inner x ", x)
    inner()
    print("Outer x: ", x)
outer()
print("Global x: ",x)