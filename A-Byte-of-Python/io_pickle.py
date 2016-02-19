# pickle is used to store plain Python object in a file
# used for later retrieval
# aka: storing the object persistently

import pickle

# name of file (which contains the object)
booklistfile = 'booklist.data'

# list of books to buy
booklist = ['The Martian', 'Open City', 'The Brief Wondrous Life of Oscar Wao', 'Being Mortal']

# Write to file (wb - write binary mode)
file = open(booklistfile, 'wb')

# Dump object to a file
pickle.dump(booklist, file)
file.close()

# Destroy booklist variable
del booklist

# Read from storage
file = open(booklistfile, 'rb')

# Load object from file
storedlist = pickle.load(file)
print(storedlist)