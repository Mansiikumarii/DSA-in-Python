'''
We can use break statement inside loop to break loop execution based on some condition. We can also use continue statement to skip the current iteration of the loop and continue with the next iteration.
'''

for i in range(10):
    if i==7:
        print("Processing stopped at i =",i)
        break

'''
Continue statement :-
We use continue statement to skip iteration and continue with the next iteration of the loop. When continue statement is encountered inside a loop, the remaining code inside the loop is skipped for the current iteration and the loop continues with the next iteration.
'''
for i in range(10):
    if i%2 == 0:
        continue
    print(i)

'''
Pass Statement :-
Pass statement is a NULL operation. It does nothing when executed. It is mainly used as a placeholder where code is syntatically required but we do not want to execute any code. For example, we can use pass statement in a function definition when we do not want to implement the function yet.
When to use pass statement?
1) Empty function or class definition
2) Empty loop body
3) When a statement is required but no action is to be performed

'''

def myfunc():
    pass

class myClass:
    pass

for i in range(5):
    pass

x = 10
if(x>5):
    pass
else:
    print("x is less than or equal to 5")

for i in range(1,9):
    if i%9 ==0:
        print(i)
    else:
        pass