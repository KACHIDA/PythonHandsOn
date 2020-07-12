""" Dictionaries - Note that we can use only immutable objects (like strings) as keys of a dictionary but we can use either immutable or mutable objects for the values for the 
	dictionary, this basically translates to say that you should use only simple objects for keys
	Pairs of keys and values are specified in dictionary, by using the notation ,  d = { key1: value1, key2: value2, key3: value3 } 
	notice the colon and curly braces,	"""


ab = {
	'swaroop':'swaroop@swaroop.ch',
	'Larry':'larry@wall.ch'
	'Matsumoto':'matz@ruby-lang.org',
	'spammer':'spammer@hotmail.com'
}

#Accessing of the elements KV pair in the dictionary
print("Swaroop's address is", ab['swaroop'])

#Remove the KV Pair from dictionary
del ab['spammer']

print('\n There are {} contacts in the address book\n'.format(len(ab)));

for name,address in ab.items():
	print('Contact {} at {} '.)
