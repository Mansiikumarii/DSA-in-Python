'''
- We can apply these operators bit by bit to integers. The result is an integer where each bit is the result of applying the operator to the corresponding bits of the operands.
- These operators are applicable only on int and bool types. If we apply these operators on bool type, then it will give the same result as logical operators.
- By mistake if we are trying to apply for any otherwise we will get TypeError: unsupported operand type(s) for <operator>: 'type1' and 'type2'
- Bitwise operators are not applicable for float and string types. If we are trying to apply for any otherwise we will get TypeError: unsupported operand type(s) for <operator>: 'type1' and 'type2'

Operators:-
& (bitwise AND)
| (bitwise OR)
^ (bitwise XOR)
~ (bitwise NOT)
<< (left shift)
>> (right shift)
'''

a= 4
b= 5
'''
0100
0101
0100 (Result of a&b)
0101 (Result of a|b)
0001 (Result of a^b)

~x = -(x+1)

'''
print(a&b)

print(a|b)
print(a^b)
print(~a) 
print(a<<2) # Left shift by 2 positions (equivalent to multiplying by 4) i.e x*2^k
print(a>>2) # Right shift by 2 positions (equivalent to integer division by 4) i.e x//2^k

'''
Shift all bits towards left by certain No. of specified bits and fill the vacated bits with 0. It is equivalent to multiplying the number by 2 raised to the power of the number of positions shifted.
'''
print(10<<2) # 10*2^2 = 10*4 = 40

x= 5
print(~x) # -(5+1) = -6
'''
Logic:
x = 0101 (5 in binary)
~x = 1010 (in binary) which is -6 in decimal (using two's complement representation)
2's complement system
MSB -> 1 => negative number
MSB ->0 => positive number
1010 => -1*2^3 + 0*2^2 + 1*2^1 + 0*2^0 = -8 + 0 + 2 + 0 = -6
'''

x = -3
print(~x)

i= 0xAE1
j = i&152
k = j|100
print(k)

'''
Given ASCII value

'A' - 'Z' : 65-90
'a' - 'z' : 97-122
'*' : 42, '+' : 43, '-' : 45, '/' : 47

'''
a= 'P'
b = 'x'
c= chr((ord(a) & ord(b)) + ord('*'))
print(c)
d = chr((ord(a) | ord(b)) - ord('-'))
print(d)
e = chr((ord(a)^ord(b))+ord('+'))
print(e)

print(f"{c} {d} {e}")