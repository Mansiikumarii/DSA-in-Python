for i in range(4):
    for j in range(4):
        print(i,j)

'''
   *
  ***
 *****
*******
'''
for i in range(4):
    for j in range(4-i):
        print(" ",end="")
    for k in range(2*i+1):
        print("*",end="")
    print()

'''
   1
  212
 32123
4321234
'''

for i in range(1,5):
    for j in range(4-i):
        print(" ",end="")
    for k in range(i,0,-1):
        print(k,end="")
    for l in range(2,i+1):
        print(l,end="")
    print()

j=1
i = 1
for i in range(1,11):
    if(i%3 != 0):
        j += 2
        continue
    if(j%3 == 0):
        break
print(i+j)

x=0
for i in  range(2,5):
    for j in range(1,i):
        x+= j
        if x%3 == 0:
            x -= i
print(x)

result = 1
for i in range(3,6):
    result *= i
    for j in range (2,i):
        if i%j == 0:
            result -= j
print(result)

squares = [x*x for x in range(5)]
result = 0
for i in squares:
    if i>5:
        result += i
        break
    result += i
else:
    result += 10
print(result)