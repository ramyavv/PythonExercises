
def f(z):
	if z==0:
		return 0
	else:
		x=0
		y=1
		for i in range (0,z):
			z=x+y
			y=x
			x=z
	return z


print(f(6))
		


			
		
