"""
Acquiring a resource in the try block and subsequently releasing the resource in the finally block is common pattern . Hence , there is also a with statement that enables this to be done in a clean manner.

The difference here is that we are using the open function with the with statement - we leave the closing of the file to be done automatically by with open.

What happens behind the scenes is that there is protocol used by with statement.It fetches the object returned by the open statement, lets call it "thefile" in this case.

It always calls the thefile.__enter__ function before starting the block of code under it and always calls thefile.__exit__ function after finishing the block of code.

So the code that we would have written in a finally block should be taken care of automatically by the __exit__ method. This is what helps us to avoid having to use explicit try..finally statements repeatedly.

"""


with open("poem.txt") as f:
	for line in f:
		print(line, end='')

