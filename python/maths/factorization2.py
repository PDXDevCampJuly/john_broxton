from sys import argv
from collections import Counter

target = int(argv[1])

with open('primes.txt') as f: 
	primes = f.read().split('\n')[:-1] 

# primes = [int(p) for p in primes]


list = []
for p in primes: 
	list.append(int(p))
primes = list


factorList = []
remainder = target
for p in primes: 
	while remainder % p == 0: 
		factorList.append(p)
		remainder = remainder / p
	if remainder == 1: 
		break

strs = []
for factor in factorList: 
	strs.append(str(factor))

print("{} =".format(target), "*".)