from collections import defaultdict

def convert(s, numRows):
    """
    :type s: str
    :type numRows: int
    :rtype: str
    """
    row = 1
    up = True
    dictionary = defaultdict(list)

    for char in s:
    	dictionary[row].append(char)
    	if up:
    		row+=1
    	else:
    		row-=1

    	if row == 1:
    		up = True
    	if row == numRows:
    		up = False

    string = ""

    for key in dictionary:
    	string += ''.join(dictionary[key])

    return string