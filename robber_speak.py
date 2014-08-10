def robber_speak(s):
	vowels_w=['a','e','i','o','u',' ']
	length=len(s)
	new_s = list(s)
	for i in range(0,len(s)):
		if new_s[i] not in vowels_w:
			new_s[i]=new_s[i]+'o'+new_s[i]
			#new_string=''.join(new_s)
	return ''.join(new_s)

	

print robber_speak("this should work without whitespace")