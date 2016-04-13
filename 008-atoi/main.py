def isNumber(c):
	try:
		int(c)
		return True
	except ValueError:
		return False

def myAtoi(string):
	return_int = 0
	string_int = ""
	sign = 1

	string.strip()

	for i, c in enumerate(string):
		if i == 0:
			if c == '-':
				sign = -1
				continue
			elif c == '+':
				continue
			elif isNumber(c):
				string_int += c
				continue
			else:
				string_int = "0"
				break

		if isNumber(c):
			string_int += c
		else:
			break

	if isNumber(string_int):
		return_int = int(string_int) * sign
	else:
		return_int = 0

  if return_int > 2147483647:
      return 2147483647
  
  if return_int < -2147483648:
      return -2147483648
        
	return return_int
