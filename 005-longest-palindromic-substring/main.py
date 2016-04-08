class Solution(object):
    def isPalindrome(self, s):
    	return s == s[::-1]
    
    def longestPalindrome(self,s):
    	longest = ""
    
    	if len(s) < 2 or self.isPalindrome(s):
    		return s
            
    	for index,letter in enumerate(s):
    		if letter in s[index+1:]:
    			ends = [i for i, x in enumerate(s[index:]) if x == letter]
    		else:
    			continue
    
    		done = False
    		
    		if((not self.isPalindrome(s[index:ends[0]+index+1])) or (len(longest) > len(s[index:ends[len(ends)-1]+index+1]))):
    		    continue

    		for i in range(len(ends)-1, -1, -1): 
    			if done:
    				break
                
    			if(self.isPalindrome(s[index:ends[i]+index+1])):
    				longest = s[index:ends[i]+index+1]
    				done = True
    					
    		if len(longest) >= (len(s)-index):
    		    return longest
    
    	return longest