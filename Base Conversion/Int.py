#It will convert data type to integer except complex data type
print(int(84.62))
print(int(True))
print(int("123"))
#print(int("Rupali")) #ValueError: invalid literal for int() with base 10: 'Rupali'
print(int('0b1010', 2))
print(int ('0xA', 16))
# print(int(2+3j)) #TypeError: can't convert complex to int