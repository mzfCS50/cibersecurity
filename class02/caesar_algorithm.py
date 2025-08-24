def encrypt():
	message = input("Type your message: ")
	message = message.upper()
	key = int(input("Type the key: "))
	cipher = ""
	for char in message:
		if char.isalpha():
			shifted = (ord(char) - ord ('A') + key) % 26 + ord('A')
			cipher += chr(shifted)	
		else:
			cipher += char
	print("The encrypted message is:")
	print(cipher)


def decrypt():
	cipher = input("Type the ciphered text: ")
	cipher = cipher.upper()
	key = int(input("Type the key: "))
	decipher = ""
	for char in cipher:
		if char.isalpha():
			shifted = (ord(char) - ord ('A') - key) % 26 + ord('A')
			decipher += chr(shifted)
		else:
			decipher += char
	print("The message is: ")
	print(decipher)

option = int(input("1- encrypt 2- decrypt: "))
if option == 1:
	encrypt()
elif option == 2:
	decrypt()
else:
	print("Invalid option!")
