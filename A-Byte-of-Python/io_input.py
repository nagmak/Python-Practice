def reverse(text):
	return text[::-1] #slicing to reverse text
	# sequence[a:b:increment value]

def is_palindrome(text):
	return text == reverse(text) #checks if reverse text is equal to original

something = input("Enter text: ")
if is_palindrome(something):
	print("Yes, it is a palindrome")
else:
	print("No it is not a palindrome")