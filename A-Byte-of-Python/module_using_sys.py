import sys

print('The command line arguments are:')

for i in sys.argv:
	print(i)

print('\n\nTHE PYTHONPATH is', sys.path, '\n')