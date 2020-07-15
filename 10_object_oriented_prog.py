"""

We designed our programs around functions i.e, block of statements which manipulate the data.this called procedure oriented way of programming. 

Another way of organizing your program which is to combine data and functionality and wrap it inside something called an object. This is called object oriented programming paradigm.

A class creates a new type where objects are instances of the class. 

Instance varaiable and class variable. A class is created using the class keyword

The Self -

Class methods have only one specific difference from ordinary functions - they must have an extra first name that has to be added to beginning of the parameter list, but you do not give a value for this parameter when you call the method,python will provide it , this particular variable refers to object itself and  by convention , it is given name self

The Self in python is equivalent to this pointer in C++ and this reference in Java and C#


Say you have a class called MyClass and an instance of this class called myobject. when you call a method of this object as myobject.method(arg1,arg2) , this is automatically converted by python into myclass.method(myobject,arg1, arg2) - this is all special self is about.
"""
class Person:
	def say_hi(self):
		print('Hello, how are you ?')

p=Person()
p.say_hi()


""" Output tells us we have instance of the person class in the __main__ module """
