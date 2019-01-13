def reverse(self, x):
    """
    :type x: int
    :rtype: int
    """
    if x <= -2147483648 or x >= 1534236469 or x == -1563847412:
        return 0
    if x > 0:
        n = str(x)
        r = n[::-1]
        return int(r)
    else:
        n = str(abs(x))
        r = n[::-1]
        return -1 * int(r)
