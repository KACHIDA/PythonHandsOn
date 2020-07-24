"""

There is special way of receiving parameters to a function as a tuple or dictionary using the * or ** prefix respectively. This is useful when taking the variable number of arguments in the function.

Because we have a * prefix on the args variable, all extra arguments passed to the function are stored in args as a tuple, if a ** prefix had been used instead, the extra parameters would be considered to be key/value pairs of a dictionary.

"""

def powersum(power, *args):
	''' Return the sum of the each argument raised to specified power.'''
	total = 0
	for i in args:
		total +=pow(i, power)
	return total

print(powersum(2,3,4))
print(powersum(2,10))
