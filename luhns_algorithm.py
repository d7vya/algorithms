#luhn's algorithm to look for the errors
card_number='4211-1611-4555-1141'#need to remove the space and the hyphen


def card_verify(reverse_card_number):
	sum_of_odd_digits = 0
	odd_digits = reverse_card_number[::2]
	for digit in odd_digits:
		sum_of_odd_digits+=int(digit)

	even_digits= reverse_card_number[1::2]
	sum_of_even_digits=0
	for digit in even_digits:
		number=int(digit)*2
		if number>=10:
			number = (number//10)+(number%10)

		sum_of_even_digits+= number
	total= sum_of_odd_digits+sum_of_even_digits
	return 0==total%10	 	


def main(card_number):
	translate_1 = str.maketrans({'-':''," ":''})#this is very important step
	card_number= card_number.translate(translate_1)
	reverse_card_number = card_number[::-1]
	if card_verify(reverse_card_number):
		print('VALID!')
	else :
		print('INVALID!')	

main(card_number)

