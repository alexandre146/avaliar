zero = int(input())
um = int(input())
dois = int(input())

if(zero > um):
	if(zero > dois):
		if(um > dois):
			print (dois)
			print (um)
			print (zero)
		else:
			print (um)
			print (dois)
			print (zero)
	else:
		print (um)
		print (zero)
		print (dois)
else:
	if(um > dois):
		if(dois > zero):
			print (zero)
			print (dois)
			print (um)
		else:
			print (dois)
			print (zero)
			print (um)
	else:
		print (zero)
		print (um)
		print (dois)