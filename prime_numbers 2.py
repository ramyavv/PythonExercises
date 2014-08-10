def sieve(n):
	a=[i for i in xrange(2,n)]
	for i in range(2,n):
		for j in range(i+1,n):
			if(j%i==0):
				if j in a:
					a.remove(j)
	return a
	

		

print sieve(10)				