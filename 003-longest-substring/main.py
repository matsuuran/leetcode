import collections 

def lengthOfLongestSubstring(s):
    """
    :type s: str
    :rtype: int
    """
    if(len(s) < 2):
    	return len(s)

    sub = ""
    maxlength = 0

    for char in s:
    	if char not in sub:
    		sub += char
    	else:
    		maxlength = max(len(sub), maxlength)
    		sub = sub[sub.find(char)+1:] + char

    return max(len(sub), maxlength)