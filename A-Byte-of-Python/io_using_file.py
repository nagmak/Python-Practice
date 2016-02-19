poem = '''\
Programming:
When the work is done
If you want your program to run:
	use Python!
'''

# Open file to write
file = open('poem.txt', 'w')

# Writing text to the file
file.write(poem)

# Close file
file.close()

# Default mode is the read mode
file = open('poem.txt')

while True:
	line = file.readline()
	#End of line = zero length
	if len(line) == 0:
		break
	print(line, end='')

# Close file
file.close()

