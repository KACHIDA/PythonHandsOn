""" Tuples are used to hold together multiple objects. 	One major feature of tuples is that they are immutable like strings ie. you cannot modify tuple

Tuples are defined by specifying items separated by commas within paranthesis

Tuples are usually used in cases where a statement or a user-defined function can safely assume that collection of values (i.e, tuple of values used) will not 
change.
 """
""" 
Tuple with 0 or 1 items
	
	A empty tuple is constructed with pair of parathensis such as myempty=() . However tuple with single item is no so simple. 	you have to specify it using the comma operator (,) , example mytup = (2,)



"""

zoo = ('Rhino','elephant','Penguin')
print("Number of anumals in the zoo :",len(zoo))
new_zoo='Monkey','Camel',zoo
print('Number of cages in the new zoo',len(zoo))
print('All animals in the zoo are',new_zoo)
print('Animals bought from old zoo are: ',new_zoo[2])
print('Last animal bought from old zoo is : ',new_zoo[2][2])
print('Number of animals in the new zoo is',len(new_zoo)-1+len(new_zoo[2]))


