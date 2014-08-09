def fact(n):
	if (n < 2):
		return 1
	else:
		for i in range (1,n):
			n=n*i
	return n

print(fact(5))