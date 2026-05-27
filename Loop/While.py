'''
A while loop is used to repeat a block of code as long as given condition is true. The syntax of a while loop is:
while condition:
    body

while condition:
    body
else:
    body
'''

i = 1
while i<= 3:
    print(i)
    i += 1
else:
  print("Loop is finished")

i = 1
while i<= 5:
    print(i)
    if i == 2:
        break
    i+= 1
else:
    print("Loop is finished")

x = 4096
count = 0
while x:
    if x & 1:
        print("GATE 2026")
        count += 1
    x>>= 1
print("Number of trailing zeros in 4096 is ", count)