"""

Notice that usage of a, b = <some expression> interprets the result of the expression as a tuple with two values.

"""

def get_error_details():
	return(2,'details')

errnum,errstr = get_error_details()
print(errnum)
print(errstr)
