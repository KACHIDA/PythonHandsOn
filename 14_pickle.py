"""

Python provides a standard module called pickle which you can use to store any plain python object in a file and then get back later. this is called storing the object persistently.

To store an object in a file, we have to first open the file in write binary mode and then call the dump function of the pickle module. This process is called pickling.

Next, we retrieve the object using the load function of the pickle module which returns the object . This process is called unpickling.

"""

import pickle

# the name of the file where we will store the object
shoplistfile = 'shoplist.data'
# The list of things to buy
shoplist = ['apple','mango','orange']


#write to file
f=open(shoplistfile,'wb')
#dump the object to the file
pickle.dump(shoplist, f)
f.close()

#destroy the shoplist varibale
del shoplist

#Read back from the storage
f=open(shoplistfile,'rb')
storedlist = pickle.load(f)
print(storedlist)
f.close()

 
