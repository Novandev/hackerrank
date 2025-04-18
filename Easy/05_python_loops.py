def python_loops(n):
    """
    The list of non-negative integers that are less than n= 3 is [0,1,2,3].
    Print the square of each number on a separate line.

    Parameters
    ----------

    Returns
    ----------
    """

    array_list = [i**2 for i in range(n)]

    return array_list



print(python_loops(10))