def isPalindrome(s):
	stringLength = len(s)-1
	for index, letter in enumerate(s):
		if(letter != s[stringLength-index]):
			return False
	return True


def longestPalindrome(s):
	longest = ""

	for index,letter in enumerate(s):
		nextString = s[index:s[index+1:].index(letter)+index+1]
		if(isPalindrome(nextString)):
			if(len(longest < nextString)):
				longest = nextString
	return longest