def convert_to_decimal(number, system):
	decnum = 0
	for i in range(len(number)):
		if number[-1].isdigit():
			digit = int(number[-1]) % 10
		else:
			digit = ord(number[-1]) - 55
		decnum += digit * system ** i
		number = number[:-1]
	return decnum


print(convert_to_decimal("1A4", 16))
