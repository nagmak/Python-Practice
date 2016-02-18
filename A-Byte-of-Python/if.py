number = 23
guess = int(input('Enter an integer: '))

if guess == number:
	#new block
	print('Congrats, you guessed it.')
	print('(but you do not win anything)')

elif guess<number:
	print('No, it is a little higher.')

else:
	print('Nope its lower than that')

print ('done')


