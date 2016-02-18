x = 50

def func(x):
	print('x is', x)
	x = 2 #only local change, does not exist outside function
	print('Changed local x to', x)

func(x)
print('x is still', x)