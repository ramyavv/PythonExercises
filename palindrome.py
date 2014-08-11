import re
def is_palindrome(s):
	s=s.lower()
	#s.replace(" ", "")
	s=re.sub('[^a-zA-Z0-9]','',s)
	l=len(s)
	list_s=list(s)
	for i in range(0,l):
		if(list_s[i] !=list_s[l-i-1]):
			return False
		else:
			return True


print is_palindrome("Sit on a potato pan, Otis")