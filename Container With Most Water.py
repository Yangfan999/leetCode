def maxArea(self, height):
    """
    :type height: List[int]
    :rtype: int
    """
    xxx = 0
    i = 0
    j = len(height) - 1
    while i != j:
        kkk = min(height[i], height[j])
        aaa = (j - i) * kkk
        if aaa > xxx:
            xxx = aaa
        if kkk == height[i]:
            i += 1
        else:
            j -= 1
    return xxx