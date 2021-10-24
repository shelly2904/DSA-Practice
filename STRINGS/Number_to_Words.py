#Convert the number to words:
#for example: 123 -> One hundred twenty three


ones = ['', 'one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine']
teens = ['ten', 'eleven', 'twelve', 'thirteen', 'fourteen', 'fifteen', 'sixteen', 'seventeen', 'eighteen', 'nineteen']
tens = ['', '', 'twenty', 'thirty', 'fourty', 'fifty', 'sixty', 'seventy', 'eighty', 'ninety']
bases = ['',  'thousand', 'million', 'billion', 'trillion', 'quadrillion']


def extract_three(number):
	places = 0
	str = ''
	while number:
		remainder = number%1000
		if convert_to_word(remainder) != '':
			str = convert_to_word(remainder) + " " + bases[places] + ' '+ str
		number = number/1000
		places += 1
	print(str)


def convert_to_word(number):
	teen = number % 100
	teen_num = extract_teen(teen)
	number = number / 100
	if number == 0:
		return teen_num
	remainder = number%10
	print(remainder)
	if remainder < 10:
		hund_num = ones[remainder] + " " + 'hundred'
	number = number/10
	return hund_num + ' ' + teen_num



def extract_teen(number):
	out = ""
	if number < 10:
		out = ones[number]
	elif number < 20:
		out = teens[number % 10] 
	else:
		out = tens[(number / 10)] + ' ' + ones[number % 10]
	return out



def num_rec(number, place):
	remainder = number %100

	if number == 0:
		return ""

	if remainder < 10:
		num = ones[remainder]
	elif remainder < 20:
		num = teens[remainder%10]
	else:
		if remainder%10 == 0:
			num = tens[remainder/10] 
		else:
			num = tens[remainder/10] + ' ' + ones[remainder%10]
	pl = bases[place]
	number /= 100
	return num_rec(number, place+1) + ' ' + num + ' '+ pl


print(extract_three(2040600000065000))





