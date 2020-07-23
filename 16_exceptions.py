"""

Exceptions occur when exceptional situations occur in your program.

"""

try:
	text = input('Enter something --> ')
except EOFError:
	print('Why did you do an EOF and me?')
except KeyboardInterrupt:
	print('You cancelled the operation.')
else:
	print('You entered{} '.format(text))

