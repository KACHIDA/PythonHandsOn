"""
Input from user
"""

def reverse(text):
	return text[::-1];

def is_palindrome(text):
	return text == reverse(text)

something = input('enter text: ')
if is_palindrome(something):
	print("Yes, it is a palindrome")
else:
	print("No, its not a palindrome")
