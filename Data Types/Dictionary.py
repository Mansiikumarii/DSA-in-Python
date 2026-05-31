#ordered
#no indexing
#data stored in key-value pair d={k:v}
# d={k1:v1, k2:v2, k3:v3........kn:vn}
# mutable : values
# keys must be immutable/unique data type and unique
# values can be of any data type and can be duplicate
'''
d = {K1 : V1; K2:V2 ; K3: V3................Kr: Vr}
''' 

d= {100 : 'Virat', 101: 'Joe Root', 103 : 'Jasprit Bumrah', 104 : 'Abhishek Sharma' , 105: 'Travis Head'}
print(d)

wc = {'India':['Suryakumar Yadav','Ishan Kishan','Virat Kohli','Jasprit Bumrah','Hardik Pandya'],
      'Australia':['Travis Head','Steve Smith','Mitchell Starc','Adam Zampa','Pat Cummins'],
      'New Zealand':['Kane Williamson','Daryl Mitchel','Finn Allen','Rachin Ravindra','Trent Boult'],
      'England':['Joe Root','Harry Brook','Will Jacks','Liam Livingstone','Mark Wood'],
      'South Africa':['Aiden Markram','Laura Wolvaardt','David Miller','Kagiso Rabada','Marco Jansen']}
print(wc)

# d = {10:'apple', 11: 20.6, True: 'Hello',(): 20,"Hi":"Hello",[] : list}
# print(d) TypeError: cannot use 'list' as a dict key (unhashable type: 'list')

#How to create a dictinory
d={}
d[100] = 'Ujjwal'
d[200] = 'Prafull'
d[300] = 'Prince'

print(d)

d = {100: 'Khushi', 200:'Shailendra', 300:'Alok'}
print(d)

'''
Creating dictionary from dict:-
Syntax:-
dict(Iterable)
'''
d= dict([(1,'Bananas'),(2,'Apples'),(3,'Strawberries'),(4,'Grapes'),(5,'Watermelon')])
print(d)

d = {1: 'Mangoes', 2: 'Peaches', 3: 'Oranges', 4: 'Pineapples', 5: 'Blueberries'}
print(d)

L = ['ap', 'xy',['p', 4]]
d = dict(L)
print(d)

'''L = ['ap','xyz',['p',4]]
d= dict(L)
ValueError: dictionary update sequence element #1 has length 3; 2 is required
'''

L = {1,'Cherry',2,'Kiwi',3,'Raspberry ', 4,'Pomegranate',5,'Avocado'}
print(L)

# d = dict(L) TypeError: object is not iterable

'''
Creating dictionary from comprehension
Syntax:-
var = {key_exp : value_exp for items}
'''

d = {i : i*i for i in range(1,5)}
print(d)
# How to access data from dictionary :-

d = {100 : 'Abhishek Sharma', 101: 'Smriti Mandhana',103:'Jasprit Bumrah',104:'Daryl Mitchell', 105:'Ellyse Perry' }
print(d[100])
print(d[101])

'''
NOTE:- dict[key]

VALID METHOS:-
keys()
sorted
values()
items()
set default()
update()
pop()
clear()
copy()
fromkeys()

NOT VALID:-
append()
insert()
sort()
add()
remove()
count()
index()
upper()
union()
slicing()
'''

#How to update dictionary
# d[keys] = values

d = {1:'Sikandar Raza', 2:'Rashid Khan', 3:'Laura Wolvaardt',4:'Hayley Matthews', 5:'Ellyse Perry'}
d[3] = 'Ashleigh Gardner'
print(d)

'''
Important function of dictionary:-
Keys(): return view of object(live window) , Syntax: d.keys() # returns dict_key(viewobject, not list)
NOTE:-
view object
1)Dynamic
2) Sharwd mwmory
3) not list
4) not editable

'''
K = d.keys()
print(K)
d[4] = 'D'
print(K)
# d.keys().append(5) AttributeError: 'dict_keys' object has no attribute 'append'

# 2) Values, return view object
d = {1:'A',2:'B',3:'C'}
V = d.values()
print(V)
d[4] = 'D'
print(V) 
