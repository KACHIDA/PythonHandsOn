"""

A lambda statement is used to create new function objects. Essentially, the lambda takes a parameter followed by a single expression. Lambda becomes the body of the function. The value of this expression is returned by the new function.


Instead of writing a separate def block for a function that will get used in only this place, we use a lambda expression to create a new function.



"""

points = [{'x':2, 'y':3},{'x':4, 'y':1}]
points.sort(key=lambda i: i['y'])
print(points)


