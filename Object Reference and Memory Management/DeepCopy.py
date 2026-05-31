'''
A deep copy creates a new object and recursivly copies all object found in original. This means the new object
is fully independent of original object, and changes made in copied object will not affect the original
object.

Key Characterstics:-
- Copies the outer structure (the container object)
- Recursivly copies all the nested objects, creating new instances for each
- Changes in copied object do not affect the original object
'''

import copy
original = [[1,2],[3,4]]
deep_copy = copy.deepcopy(original)
deep_copy[0][0] = 99
print("original: ", original)
print("Deep copy ", deep_copy)