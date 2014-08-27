#! /usr/bin/env python
# Ethan Wolfe

import sys
import random

k = 7
length = 50

source = ''
result = ''

f = open('dickens.txt', 'r')

for line in f:
	source += line.rstrip('\r\n')

f.close()

randOne = random.randint(0,len(source))
randTwo = random.randint(0,len(source))

l = 0
loops = 0
seed = ''
compare = ''
storage = ''

for i in xrange(0,k):
	seed += source[randOne + i]

while  loops < length:
	while l < len(source):
		while l < k:
			compare += source[l]
			l = l + 1
		if seed.lower() == compare.lower():
			storage += source[l]
			#print 'Match Found!'
		#print seed + ' == ' + compare
		compare = compare[1:]
		compare += source[l]
		l = l + 1
	#print 'Text Looped ' + str(loops)
	if len(storage) == 0:
		seed = ''
		randTwo = random.randint(0,len(source))
		for i in xrange(0,k):
			seed += source[randTwo + i]
	else:
		randOne = random.randint(0,len(storage)-1)
		result += storage[randOne]
		seed = seed[1:]
		seed += storage[randOne]

	loops = loops + 1
	

	storage = ''
	l = 0
	compare = ''

print result

f2 = open('output.txt', 'w')

f2.write(result)
f2.close()

