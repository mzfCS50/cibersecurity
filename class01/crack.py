from string import digits, ascii_letters, punctuation

def passcode_crack():
	for i in digits:
		for j in digits:
			for k in digits:
				for l in digits:
					print(i, j, k, l)

def alphabet_crack():
	for i in ascii_letters:
		for j in ascii_letters:
			for k in ascii_letters:
				for l in ascii_letters:
					print(i, j, k, l)

def special_characters_crack():
	for i in digits + ascii_letters + punctuation:
		for j in digits + ascii_letters + punctuation:
			for k in digits + ascii_letters + punctuation:
				for l in digits + ascii_letters + punctuation:
					print(i, j , k, l)

option = int(input("1 - passcode_crack 2 - alphabet_crack 3 - special_characters_crack: "))

if option == 1:
	passcode_crack()
elif option == 2:
	alphabet_crack()
elif option == 3:
	special_characters_crack()
else:
	print("Invalid option bitch")
