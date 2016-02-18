age = 20
name = 'Nagma'

print('{0} was {1} years old when she wrote a book'.format(name,age))
print('Why is {0} playing with that python?'.format(name))

#format method used to substitute specs with arguments

#{0} corresponds to variable name
#{1} corresponds to variable age

#same with string concatenation
print(name + ' is ' + str(age) + ' years old') #not recommended/ugly

#numbers in the curly braces are optional
#can be written like this too:

print('{} was {} years old when she wrote a book'.format(name, age))

#More detailed specs using format method
print('{0:.3f}'.format(1.0/3)) #decimal precision to 3, for flot 0.333

#fill with underscores with text centered
print('{0:_^11}'.format('hello'))

#keyword-based

print('{name} wrote {book}'.format(name='Swaroop', book='A Byte of Python'))

#in python \n is automatically done for print

#ESCAPE SEQUENCE '\' FOR things like apostrophes in a sentence
# 'What\'s your name?'
# 'This is the first line\nThis is the second line'
# 'This is the first sentence. \ This is the second sentence'

#RAW STRING
