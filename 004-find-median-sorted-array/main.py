def findMedianSortedArrays(nums1, nums2):
    """
    :type nums1: List[int]
    :type nums2: List[int]
    :rtype: float
    """

    array = []
    median = 0
    lengthTotal = len(nums1) + len(nums2)

    if(lengthTotal%2==0):
    	j = lengthTotal/2 + 1
    else:
    	j = int(lengthTotal/2)+(lengthTotal%2)

    for i in range(0,j):
    	if(len(nums1)==0):
    		array.append(nums2.pop(0))
    	elif(len(nums2)==0):
    		array.append(nums1.pop(0))
    	elif(nums1[0] < nums2[0]):
    		array.append(nums1.pop(0))
    	else:
    		array.append(nums2.pop(0))


    if(lengthTotal%2 == 0):
    	median = (float(array[len(array)-1] + array[len(array)-2])/2)
    else:
    	median = array[len(array)-1]


    return median