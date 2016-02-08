def singleNumber(nums):
	d = {}
	for num in nums: 
		if d.has_key(num):
			del d[num]
		else:
			d[num] = 1
	return d.keys()[0]
