print("Hello")
print('Hi')
print("Ashiana Umang")
print("abcd")
print("abcd\nefgh")
print("Ashiana\nUmang")
print("ab\tcd\nef\tgh")
print("ab\\tcd\nef\ngh")

'''
String is a sequence of immutable characters. It is a collection of characters enclosed in single quotes, double quotes or triple quotes. String can be defined using single quotes, double quotes or triple quotes. Triple quotes are used to define multi-line strings.
'''
s = "python"
print(s[2])
print(s[-4])
print(s[-4+6])
#print(s[6]) Error: IndexError: string index out of range
# s[4] = 'A' Error: TypeError: 'str' object does not support item assignment

s = s+'!' # New object is created in separate memory box and s is now reference to new object. Old object is garbage collected.
print(s)

# String Operations
print("Prince" + "HCL-2026")
print("Shruti"*3)
print("Ujjwal"*0)
print("Jaydeep" * -5)

'''
print("Shrishti"*2.5) # TypeError: can't multiply sequence by non-int of type 'float'
print("Vishal"-"Vaishali") # Error : unsupported operand in string 
print(Parul / Bhadoria)  # Error : unsupported operand in string 

Common String methods:-
* upper()
* lower()
* title()
* capitalize()

Synatx to apply method:-
var.method()
value.method()
expr.method()

all these are stored in seprate memory box
'''

a = "bharat"
b = "India"
print(a.upper())
print("bharat".upper())
print((a+b).upper())

print(a)
a = a.upper()
print(a)

s= "hello"
print(s.upper())

# 2. Lower
s = "Hello"
print(s.lower())

# 3. Title
s = "hello world"
print(s.title())

# 4. Capatilize()  : First charachter upper , rest lower

# Seaching method
# 5. find
# Return index of occurance or -1

s= "hello world"
print(s.find("world"))
print(s.find("Java"))

# 6. Index(sub)
s = "Hello"
print(s.index("e"))
# print(s.index("A")) # Error : substring not found

# 8. count(sub) : non overlapping
# count number of occurrances
s = "banana"
print(s.count("a"))

s="aaaaa"
print(s.count("a"))
print(s.count("aa"))
print(s.count("aaa"))

# String check method (Boolean)
# 9) isalpha() : only alphabets ?

print("Hello".isalpha())
print("Hello123".isalpha())

# 10) isdigit() : only digit
print("123".isdigit())
print("12a".isdigit())

# 11) isalnum() : Alphabets + numbers ?
print("abc123".isalnum())
print("abc".isalnum())

# 12) isspace() : only space ?
print(" ".isspace())

# 13) islower() / isupper() : checks lower/ uppercase
print("hello".islower())

# Replace & Modify
# 14) replace(old, new)
s="I love Java"
print(s.replace("Java", "Python"))

# 15) strip()
'''
Remove spaces from both sides 
lstrip() - removes left spaces
rstrip() - removes right spaces
"   Hello   "
By default it removes white spaces , new line ("\n") and tab spaces ('\t')
'''

text = "\n\t     python"
print(text.lstrip())
print(text is text.lstrip())

s = "   Hello"
s1 = s.lstrip()
s2 = s.rstrip()
s3 = s.strip()
print(s)
print(s1)
print(s2)
print(s3)
print(s is s3)

'''
Syntax:-
String.(strip([char]))
char is optional
'''

text = "###@@@Welcome@@@###"
result = text.lstrip("@#")
print(text is result)
result = text.lstrip("$")
print(text is result)

# Splitting and Joining
'''
split(sep) : By default separator is space
splits String into list
'''
s = "a,b,c"
print(s.split(","))

'''
8) Join (iterable)
Adds a separator between elements 
'''
print("_".join("abc"))

'''
Other Useful Methods
Starts with (sub)/ ends with ()

String Slicing
S[begin: end: step]
begin: inclusive
end : exclusive
step : +ve/-ve but not 0

if step value is positive it should be forward direction (left to right) and we have to consider begin to end -1

'''
s = "python"
print(s[0:4:1])

'''
If -ve then it should be backward direction (Right to Left) and we have to consider begin to end+1
'''
print(s[-1: -5 : -1])

'''
In forward direction
-> default value for begin : 0
-> default value for end : length of string
-> default value of step : +1

'''
print(s[ : : ])
print(s[0: 6: 1])

'''
In backward direction
-> default value for begin : -1
-> default value for end :- (length of string)
-> default value for stop : -1
'''
print(s[ : : -1])
print(s[-1: -7: -1])

'''
NOTE:-
1) In the forward direction if end value is -1 then result is always empty Eg: [-1 : -1 : -1]
2) In the forward direction if end value is 0 the result is always Empty Eg: [0: 0: 1]
'''

print(s[ : -1])
print(s[-1: ])
print(s[ : -1 : ])

s = "python"
print(s[0: 5 : 2])
print(s[2:5:1])
print(s[4:0:-1])
print(s[1:5:1])
print(s[-5 : 5 : 1])
print( s[1 : -1 : 1])
print(s[1 : -1 : -1])
print(s[5 : -5 : 1])
print(s[ :: ])
print(s[1: -1])
print(s[2 : 2: 1])
print(s[1 : 5: ])
print(s[ : 2 : -1]) # when negative index it starts from other end s[start=last_index : stop=2 : step=-1]
print(s[2 :: -1])
print(s[ :: -1])

a = [6,5,4,3,2,1,0]
b = "AuGGTssE"
c = b[a[-3]] + b[ :: 4] + b[-1: ]
d = int((a[1]*a[2]*a[-3]*a[4//2])/4-14)
x = str(c) + str(d)
print(x)   

b = "AuGGTssE"
print(b[::4])

'''
String formatting:-
using variable / expression inside a string
'''
a = int(input("enter a = "))
b = int(input("Enter b = "))
msg = "mul of "+ str(a) + " and "+ str(b) + " is " + str(a*b)
print(msg)


# using named parameters
msg = "mul of {i} and {j} is {k}".format(i=b, j=a, k= a*b)
print(msg)

'''
WAP to print table of a given no.
5 x 1 = 5
5 x 2 = 10
5 x 3 = 15
.
.
.
.
.
.
.
.
.
.


'''

num = int(input("Enter a number"))
for i in range(1,11):
    print(f"{num} x {i} = {num * i}")
    i += 1