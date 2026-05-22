'''
Special operators are of two types:
1. Identity Operators: These operators are used to compare the memory locations of two objects. They are denoted by the symbols 'is' and 'is not'. The 'is' operator returns True if both operands refer to the same object in memory, while the 'is not' operator returns True if they refer to different objects.
2. Membership Operators: These operators are used to test whether a value is present in a sequence (such as a list, tuple, or string). They are denoted by the symbols 'in' and 'not in'. The 'in' operator returns True if the specified value is found in the sequence, while the 'not in' operator returns True if it is not found.
r1 is r2 return True of both r1 and r2 refer to the same object in memory
r1 is not r2 return True if both r1 and r2 of different objects in memory

'''

a= 10
b= 99
print(a is b) # False
print(a is not b) # True

'''
We can use is operator for Address comparison where == operator for content comparison.
'''

L1 = [1,2,3]
L2 = [1,2,3]
print(L1 is L2) # False
print(L1 == L2) # True

# Membership Operators
'''
We can use membership operators to check if a value is present in a sequence (like list, tuple, string).
in: Returns True if the specified value is found in the sequence.
not in: Returns True if the specified value is not found in the sequence.
'''

List1 = ["Gunjan", "Aahana","Tanushree", "Parul"]
print("Gunjan" in List1) # True
print("Bhunja" in List1) # False