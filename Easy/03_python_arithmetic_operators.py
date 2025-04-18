

def arithmetic_operators(a, b):
    """
        The first line contains the sum of the two numbers.
        The second line contains the difference of the two numbers (first - second).
        The third line contains the product of the two numbers.


        Parameters
        ----------
        a : the first variable
        b: the second variable

        Returns
        ----------
        String
            A representation of the three operators 
    """
    return f"{a + b}\n{a-b}\n{a*b}"



print(arithmetic_operators(5,7))