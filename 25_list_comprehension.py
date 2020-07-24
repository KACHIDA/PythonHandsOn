"""

List comprehensions are used to derive a new list from existing list. supposeyou have list of numbers and you want to get a corresponding list with all the numbers multiplied by 2 only when the number itself is greater than 2. List comprehensions are ideal for such situations.

We derive a new list by specifying the manipulation to be done(2*i) when some condition is satisfied (if i>2). note that the original list remains unmodified.

The advantage of using list comprehensions is that it reduces the amount of boilderplate code required when we use loops to process each element of a list and store in a new list.

"""

list1=[2,3,4]
list2=[2*i for i in list1 if i>2]
print(list2)

