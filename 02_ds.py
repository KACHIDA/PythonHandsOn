"""List is data Structure that holds ordered collection of item
	i.e, you can store a sequence of items in a list.
	Shopping list. List of items needs to be enclosed in the brackets
	Once created a list , it can be added, removed or search for items 
	in the list. Since we add and remove items, we can say the list is 
	mutable datatype. i.em this type can be altered.
	Python provides append method for the list class which allows you to
	add an item to end of list.
"""

""" Intro to Objects and classes -
	A list is example for objects and classses. by declaring i equal to 5 , 	An instance of int class is created (i.e, object) """

shoplist = ['apple','mango','carrot','radish']
print('I have',len(shoplist),'Items to Purchase')
print('These items are :')
for item in shoplist:
	print(item)
print('I have also want to buy rice')
shoplist.append('rice')
print('My Shopping list is now',shoplist)

print('I will sort the my list now')
shoplist.sort()
print('Sorted Shopping list is',shoplist);
print('The first item I will buy is ',shoplist[0])
olditem=shoplist[0]
del shoplist[0]
print('I bought the',olditem)
print('My Shopping list is now',shoplist)
