a = [4,5]
b = a
b[0] = 1
print(a)

a = [4,5]
b = a[:]
b[0] = 1
print(a)
print(b)

L1 = [1,2,3]
L2 = L1
L3 = [L1, L1, L1] #copies refernce
L1[0] = 5
print(L3[0])

L1 = [1,2,3]
L2 = L1
L3 = [L1[:], L1[:], L1[:]] # copies content
L1[0] = 5
print(L3[0])

L1 = [1,2,3]
L2 = L1
L3 = [L1[ : ], L1[:],L1[:]]
L1[0] = 6
print(L3)

L1 = [1,2,3]
L2 = L1
temp = L1[:]
L3 = [temp, temp, temp]
L3[0][0] = 6
print(L3)

a = [[1,2,3],[4,5,6],[7,8,9]]
b = a[1:]
b[0] = [10,11]
b[1][0] = 99
print(b)
print(a)
