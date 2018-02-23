vowels = ['a','e','i','o','u']
word = input("Provide the word: ")
found={}
#for vowel in vowels:
#	found[vowel]=0
#print(found.items())
for letter in word:
	if letter in vowels:
		found.setdefault(letter,0)
		found[letter]+=1
		#if letter in found:
		#	found[letter]+=1
		#else:
		#	found[letter]=1
for k,v in sorted(found.items()):
	print(k," was found ", v , " time (s).")	
