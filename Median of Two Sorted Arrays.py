def findMedianSortedArrays(self, nums1, nums2):
    """
    :type nums1: List[int]
    :type nums2: List[int]
    :rtype: float
    """
    m = nums1 + nums2
    m.sort()
    c = len(m)
    if c % 2 == 1:
        return m[int(c / 2)]
    a = c // 2
    return (m[a - 1] + m[a]) / 2