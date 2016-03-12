print ('Your pets have been waiting!')

# owl, toad, cat, rat

owl = {
	'name': 'Hedwig',
	'hungry': True,
	'food': 0,
	'age': 2,
	'image': '\~\(OVO)/~/',
}

toad = {
	'name': 'Trevor',
	'hungry': True,
	'food': 0,
	'age': 4,
	'image': '[>__<]',
}

cat = {
	'name': 'Crookshank',
	'hungry': False,
	'food': 1,
	'age': 10,
	'image': '[o-^-o]',
}

rat = {
	'name': 'Scabbers',
	'hungry': False,
	'food': 1,
	'age': 40,
	'image': '(*...*)',
}

magipets = [owl, toad, cat, rat]

def play(choosepet):
	if choosepet == 1:
		print ('You say "Hey ' + owl['name'] + '!" while ruffling her feathers softly.\nShe blinks contentedly.')
		print (owl['image'])
	elif choosepet == 2:
		print ('You say "Hey ' + toad['name'] + '!" while rubbing a finger over his head.\nHe sticks out his tongue.')
		print (toad['image'])
	elif choosepet == 3:
		print ('You say "Hey ' + cat['name'] + '!" giving her a baby rattle to play with.\nHe mewls.')
		print (cat['image'])
	elif choosepet == 4:
		print ('You say "Hey ' + rat['name'] + '!" while whispering a spell to turn him yellow.\nHe squeaks! Nothing happens. Someone tricked you with a fake spell. Gah.')
		print (rat['image'])
	else:
		print ('Selection error. You did not play :(')

def feed():
	for pet in magipets:
		if pet['hungry'] == True:
			print ("You fed " + pet['name'])



print ('---------------------------------')
action = str(input("Would you like to 'play' or 'feed' a pet? "))
if action == 'play':
	choosepet = int(input("Who do you want to play with? 1. owl, 2. toad, 3. cat, 4. rat: "))
	play(choosepet)
elif action == 'feed':
	feed()
else:
	print ('Selection error.')
		