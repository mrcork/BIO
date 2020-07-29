def check(password):
	password = password.upper()
	for i in range(len(password)):
		for x in range(1,len(password)-i):
			if password[i:i+x] == password[i+x:i+x+x]:
				return 'Rejected'
	return 'Accepted'

p = input()
print(check(p))

