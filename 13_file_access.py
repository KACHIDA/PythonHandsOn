"""
We can open and use file for the reading and writing by creating the object of the file class and using its read, readline or write methods appropriately to read from the file or write to the file. The ability to read or write to the file depends on the mode you have specified for the file opening. then finally, when you are finished with the file, you call the close method to tell python that we are done using the file.

"""

poem = '''\

Programming is fun
when work is done
if you wanna make your work also fun:
 use python!
'''

#open for 'w'riting

f = open('poem.txt','w')
#write text to file
f.write(poem)
# close the file
f.close()


f=open('poem.txt')
while True:
	line = f.readline()
	# Zero length indicates EOF
	if len(line) == 0:
		break
	print(line,end='')
f.close()




