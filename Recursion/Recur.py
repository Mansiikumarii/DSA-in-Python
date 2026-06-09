def A(n):
    if n==0:
        return
    print(n, end=" ")
    A(n-1)
    print(n, end=", ")
A(4)
