'''
Added to python 3.10.90
Similar to switch in C programming language. It is used to match a value against a pattern and execute the corresponding code block. It is more powerful than switch statement as it can match complex patterns and can also be used with classes and objects.
Syntax:
match expression:
    case pattern1:
        stmt1
    case pattern2:
        stmt2
    case _:
        stmt

_ => default case (like else in if-else statement)
we can write it as case default or case _ but it is recommended to use case _ as it is more readable and consistent with other pattern matching constructs in python.
match <expression>:
    case <pattern1>:
        <stmt1>
    case <pattern2>:
        <stmt2>
    case _:
        <stmt>
'''

num = 15
match num:
    case x if x<0:
        print("Negative number")
    case x if x==0:
        print("Zero")
    case x if x>0:
        print("Positive number")

'''
NOTE:-
match , case and default are not Python keywords, but the interpreter treats them as special words.
You can use match, case and default as variable names, but it is not recommended as it can lead to confusion and readability issues. 
'''

day = "Sat"
match day:
    case "Mon" | "Tue" | "Wed" | "Thu" | "Fri":
        print("Weekday")
    case "Sat" | "Sun":
        print("Weekend")
