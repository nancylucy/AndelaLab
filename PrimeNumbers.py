import math

def main():
	count = 3

	while True:
		isPrime = True

		for num in range(2, int(math.sqrt(count) + 1)):
			if count % num == 0:
				isPrime = False
				break

		if isPrime:
			print count 

		count += 1