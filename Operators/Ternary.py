'''
Syntax: condition ? expression_if_true : expression_if_false
'''

a,b,c = 10,20,30
x = a if a<b and a<c else b if b<c else c
print(x) # 10
x=3 
y=4
z= 2
a= (x if x>z else z) if x>y else (y if y>z else z)
print(a) # 4