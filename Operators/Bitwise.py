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
b= 3
print(a&b)
