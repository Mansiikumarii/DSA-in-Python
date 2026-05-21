'''
    and , or, not
    For boolean type behaviour:
    and => if both argumnets are True then only result is True otherwise False
    or => if at least one argument is True then result is True otherwise False
    not => complement operator, it will convert True to False and False to True
    E1{True} and E2{False} => False
'''

# For non boolean type behaviour:
'''
0/ 0.0/ " "/ None => False
Non zero/ non empty string/ non None => True
Eg: {-1, -0.75, 5.2, -8.2, "hii"}

# x and y:-
if x is false , then x , else y
Eg: 10 and 20 => 20

if x is evaluated to False return x otherwise return y
'''
print(10 and 20)
print(0 and 30)
print(20 and 0)

'''
x or y:-
if x is true, then x, else y
if x evaluates to True then result is x, otherwise result is y
'''
print(10 or 20)
print(0 or 20)
print(20 or 0)

print("mansi" and "mansi kumari")
print("" and "mansi kumari")
print("mansi" and " ")
print("mansi" or "mansi kumari")
print("mansi" or " ")
print(" " or " ")

'''
Short circuiting concept is applicable in logical operator
True or anything => True
NOTE:-
Case 1:- exp1 or exp2 and exp3
Step 1:- Put brackets according to precedence rule
Step 2:- Evaluates from left to right
'''

print(1 or 0 and 0)
print(0 and 0 or 1)

b=1
c=1
d=0
if(0 and 0 == 0):
    print("1 Mansi")

if(b or b-1 == 0):
    print("2 Mansi")

if(c or c-1 == 0):
    print("3 Mansi")

if(d or d+1 == 0):
    print("4 Mansi")