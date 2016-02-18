number = 23
running = True

while running:
	guess = int(input('Enter an integer: '))

	if guess == number:
		print('Congrats you are right.')
		running = False
	elif guess <number:
		print('No it is higher than that')
	else:
		print('No it is lower than that')
else:
	print('While loop is over')

print('Done')