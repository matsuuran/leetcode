def twoSum(nums, target):
    """
    :type nums: List[int]
    :type target: int
    :rtype: List[int]
    """
    if(len(nums) < 2):
        return
    
    dictionary = {}

    for index, number in enumerate(nums):
        if dictionary.get(target-number) != None:
            return [index, dictionary.get(target-number)]

        dictionary[number] = index

    return