import random
import math
import string

chars = string.ascii_letters + '0123456789'

def generateWords(number): #selects random words from the wordlist and returns them as a list

	indexes = []

	for x in range(0,number):
		indexes = indexes + [random.randint(1,102305)];

	with open('american-english') as f:
		lines=f.readlines()


	words = []
	for i in indexes:
		words = words + [lines[i][:-1] + ' ']

	return [word.replace('\'','') for word in words]

def calculatePassphraseBitsOfEntropy(number): #bits = 1 + log2(entropy)
	entropy = math.pow(102305,number)
	bits = 1 + math.log(entropy,2)
	return bits

def calculateRandomCharactersForEntropy(number): #nr of chars = log62(entropy)
	entropy = math.pow(102305,number)
	characters = math.log(entropy,62)
	return characters

def taskA():
	num = raw_input('Choose a number: ')

	try:
	    number = int(num)
	except ValueError:
	    print("Invalid number")

	words = generateWords(number)

	print ''.join(words)

	print str(number) + ' random words from a word list of 102305 words'

	print 'Entropy: ' + str(calculatePassphraseBitsOfEntropy(number)) + ' bits'

	print 'You need ' + str(calculateRandomCharactersForEntropy(number)) + ' RANDOM characters in [a-zA-Z0-9] to get the same entropy'

def generatePassphrase(bitsOfEntropy):
	entropy = pow(2,bitsOfEntropy-1)
	numberOfWords = 1
	while(pow(102305,numberOfWords) < entropy): 
		numberOfWords += 1
	return generateWords(numberOfWords)

def generatePassword(bitsOfEntropy):
	entropy = pow(2,bitsOfEntropy-1)
	numberOfCharacters = 1
	while(pow(62,numberOfCharacters) < entropy):
		numberOfCharacters += 1
	password = ''
	for i in range (0,numberOfCharacters):
		password += random.choice(chars)
	return password


def taskB():
	ent = raw_input('Choose a number: ')

	try:
	    bitsOfEntropy = float(ent)
	except ValueError:
	    print("Invalid number")

	print 'For ' + str(bitsOfEntropy) + ' bits of entropy, I suggest the passwords:' 
	print ''.join(generatePassphrase(bitsOfEntropy))
	print 'or'
	print generatePassword(bitsOfEntropy)


taskA()
taskB()