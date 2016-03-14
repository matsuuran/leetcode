def twoSum(nums, target):
    """
    :type nums: List[int]
    :type target: int
    :rtype: List[int]
    """
    if(len(nums) < 2):
      return
    
    for i, n1 in enumerate(nums):
    	for j, n2 in enumerate(nums):
    		if i == j:
    			continue

    		if n1+n2 == target:
    			return [i,j]

    return