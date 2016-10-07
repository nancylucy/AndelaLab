firstNum = 0
lastNum = int(raw_input("Enter the last number:"))

def F(n):
	if n < 2:
		return n
	else:
		return F(n-1) + F(n-2)

print map(F, range(firstNum, lastNum))