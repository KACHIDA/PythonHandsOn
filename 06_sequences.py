""" Lists, Tuples, Strings are examples of the sequences
	Major features are membership tests, (i.e, in and not in expressions)
	and indexing operations which allows us to fetch a particular item in
	the sequence directly.
	The three types of sequences mentioned above - lists, tuples and strings	also have a slicing operation which allows us to retrieve a slice of sequence i.e, part of the sequence

"""

shoplist=['apple','mango','carrot','banana']
name = 'swaroop'

#Indexing or 'Subscription' operation #
print('Item 0 is ', shoplist[0])
print('Item 1 is ', shoplist[1])
print('Item 2 is ', shoplist[2])
print('Item 3 is ', shoplist[3])
print('Item -1 is ', shoplist[-1])
print('Item -2 is ', shoplist[-2])

#slicing on a list #
print('Item 1 to 3 is', shoplist[1:3])
print('Item 2 to end is',shoplist[2:])
print('Item 1 to -1 is',shoplist[1:-1])
print('Item start to end is',shoplist[:])

#slicing on string#
print('characters 1 to 3 is',name[1:3])
print('characters 2 to end is',name[2:])
print('characters 1 to -1 is ',name[1:-1])
print('characters from start to end is ',name[:])


