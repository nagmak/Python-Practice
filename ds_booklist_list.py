booklist = ['Harry Potter & the Half Blood Prince', 'One Hundred Years of Solitude']

print('I have', len(booklist), 'books in my library')

print('\nThese books are: ', end=' ')
for book in booklist:
	print(book, end=' ')
addbook = input('\nWhat book do you want to add? ')
booklist.append(addbook)
print('\nMy library is now', booklist)


