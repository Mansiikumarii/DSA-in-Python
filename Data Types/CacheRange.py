#CacheRange - 5 to 256
# Run it in IDLE shell to check the output 
# Here it will take entire code as a single block and execute it. So we will get the output of all the print statements at once which will return True in both cases.
a = 100
b=100
print(id(a) == id(b))

a= 300
b=300
print(id(a) == id(b))