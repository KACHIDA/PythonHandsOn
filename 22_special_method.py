"""

There are certain methods such as __init__ and __del__ methods which have special significance in classes.

Special methods are used to mimic certain behaviour of built in types. For example, if you want to use x[key[ indexing operation for your class, then all you have to do is implement the __getitem__() method and your job is done.


Some useful special methods are listed in the following table.

__init__(self, ...)
	This method is called just before the newly created object is returned for the usage.

__del__(self, ...)
	Called just before the object is destroyed (which has unpredictable timing, so avoid using this)

__str__(self, ..)
	called when we use the print function or when str() is used.

__lt__(self,other)
	called when less than operator (<) is used. similarly, there are special methods for all the operators(+,>..etc)

__getitem__(self,key)
	called when x[key] indexing operation is used

__len__(self)
	called when the built in len() function is used for the sequence object

"""

