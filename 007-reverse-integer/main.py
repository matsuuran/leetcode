def reverse(x):
    """
    :type x: int
    :rtype: int
    """
        
    if x < 0:
        integer_string = str(x)
        reverse_string = integer_string[:0:-1]
        return_int = int(reverse_string) * -1
    else:
    	integer_string = str(x)
    	reverse_string = integer_string[::-1]
    	return_int = int(reverse_string)

    if return_int > 2147483647 or return_int < -2147483647:
        return 0
        
    return return_int