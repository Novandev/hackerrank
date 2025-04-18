def python_print(n):

    """

    This function prints all numbers in a string from 1 - n, inclusive
    
    Parameters
    ----------
    n: the stopping point for the interation

    Returns
    ----------
    
    """
    

    return ''.join([str(i) for i in range(1, n+1)])



print(python_print(10))