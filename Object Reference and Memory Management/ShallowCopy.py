'''
A shallow copy creates a new object , but not recursively copy nested object within it. Instead it 
inserts a reference to original object found in original. This means the changes to mutable nested
object is the copied object will affect the original object, and vice versa.

Key characterstics :-
- copies the outer structure (the container object) # seperate memory box
- Nested objects (like list or dictionaries within container) are not coped; refernces to original
nested objects are inserted.
- changes to mutable nested objects in the copied object within object will reflect in the original object.
'''

import copy
original = [[1,2],[3,4]]
shallow_copy = copy.copy(original)
shallow_copy[0][0] = 99
print("original: ",original)
print("shallow copy: ", shallow_copy)
