def isPalindrome(s):
	stringLength = len(s)-1
	for index, letter in enumerate(s):
		if(letter != s[stringLength-index]):
			return False
	return True


def longestPalindrome(s):
	longest = ""

	for index,letter in enumerate(s):
		if letter in s[index+1:]:
			ends = [i for i, x in enumerate(s[index:]) if x == letter]
		else:
			continue

		for end in ends: 
			if(isPalindrome(s[index:end+index+1])):
				if(len(longest) < len(s[index:end+index+1])):
					longest = s[index:end+index+1]
			else:
				break

	return longest