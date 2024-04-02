#vigenere algorithm - using a key to encrypt or decrypt
text= "Vigenere Algorithm!"
custom_key="Divya Paliwal"

def vigenere(text, key,direction=1):
	key_index = 0
	alphabet = 'ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz'
	final_message=''

	for char in text:

		# Append any non-letter character to the message
		if not char.isalpha():
			final_message+=char
		else:
			# Find the right key character to encode/decode
			index_char= key[key_index%(len(key))]
			key_index+=1

			# Define the offset and the encrypted/decrypted letter
			offset = alphabet.find(index_char)
			index = alphabet.index(char)
			final_index = ((index+offset*direction)%len(alphabet))
			final_message += alphabet[final_index]

	return final_message


def encrypt(text,custom_key):

	return vigenere(text,custom_key)


def decrypt(text,custom_key):

	return vigenere(text,custom_key,-1)

encrypted=encrypt(text,custom_key)
decrypted= decrypt(encrypted,custom_key)

print(f'encrypted message : {encrypted}')
print('decypting the above message will give the original text')
print(f'decrypted message: {decrypted}')