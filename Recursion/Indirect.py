def A(n):
    if n<=1:
        return
    else:
        B(n-2)
        print(n)
        B(n-1)
        print(n-2)
def B(n):
    if n<=1:
        return
    else:
        print(n-3)
        A(n-1)
        A(n-2)
A(4)