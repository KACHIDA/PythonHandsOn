"""
Input from user
"""
import re

def reverse(text):
	return text[::-1];

def is_palindrome(text):
	return text == reverse(text)

something = input('enter text: ')
modifiedText = re.sub('[\W_]+','',something)
print('modifiedText',modifiedText);
if is_palindrome(modifiedText.upper()):
	print("Yes, it is a palindrome")
else:
	print("No, its not a palindrome")
