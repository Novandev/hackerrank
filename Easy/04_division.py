
def division(a, b):
    """
    Add logic to print two lines. The first line should contain the result of integer division,  // . The second line should contain the result of float division,  / .

    No rounding or formatting is necessary.


    Parameters
    ----------
    a: the nominator

    b: the denominator


    Returns
    ----------
    String
        The first line uses integer division while the second will use decimal based division
    """


    return f"{a//b}\n{a/b}"



print(division(10,3))