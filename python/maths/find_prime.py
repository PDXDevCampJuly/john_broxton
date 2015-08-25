#
#  This program inputs a number prints out the primes of that number in a text file 
#
###################################################################################

import math

maximum = eval(input("Please enter a number. >>> "))
primes = []
if maximum > 1: 
	for candidate in range(2, maximum + 1):
		is_prime = True
		for factor in range(2, candidate): 
			if candidate % factor == 0:
				is_prime = False
				break
		if is_prime:		
			primes.append(candidate)		

newFile = "\n".join(map(str, primes))

with open('primes.txt', 'w') as f:
	f.write(newFile)
	
def factors(n):
	fact=[1,n]
	check=2
	rootn=math.sqrt(n)
	while check<rootn:
		if n%check==0:
			fact.append(check)
			fact.append(n/check)
		check+=1
	if rootn==check:
		fact.append(check)
		fact.sort()
	return fact
	print(fact)

factors(100)