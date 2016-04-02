import collections 

def lengthOfLongestSubstring(s):
    """
    :type s: str
    :rtype: int
    """
    if(len(s) < 2):
    	return len(s)

    substring = ""
    maxlength = 0

    for c in s:
    	if c not in s:
    		substring += c
    	else:
    		maxlength = max(len(substring), maxlength)
    		substring = [substring.find(c)+1:] + c

    return max(len(substring), maxlength)