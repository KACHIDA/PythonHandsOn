"""

When data is sent over the internet , we need to send it in bytes... something your computer easily understands, The rules for translating Unicode to bytes is called encoding. A popular encoding to use is UTF-8. We can read and write in UTF-8 by using the simple keyword argument in our open function.



"""


#encoding=utf-8

import io

f=io.open("abc.txt","wt",encoding="utf-8")
f.write(u"imagine non-english language here")
f.close()

text = io.open("abc.txt",encoding="utf-8").read()
print(text)


