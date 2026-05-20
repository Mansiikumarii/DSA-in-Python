#Decimal no : base 10
#Binary no : base 2 (0 , 1)
# Octal no : base 8(0 to 7)
# Hexadecimal : base 16 (0 to 9 , A, B, C, D, E, F)

# Build in function
# bin(int) : Binary no
# oct(int) : Octal no
# hex(int) : Hexadecimal no
# int must be integer or boolean

print(bin(10))
print(oct(int(10)))
print(hex(int(10)))

# int (str, base) : to convert any no system to decimal no

a=10
s1 = bin(a)
print(s1)
s2 = int(s1, 2)
print(s2)
