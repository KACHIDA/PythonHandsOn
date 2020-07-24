"""

The Assert statement is used to assert that something is true. For example if you are very sure that you will have at least one element in a list you are using and want to check this, raise an error if its not true, then assert statement is ideal in this situation. when the assert statement fails, an AssertionError is raised The pop() method removes and returns the last item from list.

The Assert statement should be used judiciously. Most of the time, it is better to catch exceptions, either handle the problem or display an error message to the user and then quit.

"""


mylist=['item']
assert len(mylist) >=1
mylist.pop()
assert len(mylist)>=1
