def removeElement(self, nums, val):
    """
    :type nums: List[int]
    :type val: int
    :rtype: int
    """
    i, j = 0, len(nums) - 1
    
    while i <= j:
        if nums[i] == val and nums[j] != val:
            nums[i], nums[j] = nums[j], nums[i]
            j -= 1
            i += 1
        elif nums[i] == val:
            j -= 1
        elif nums[j] != val:
            i += 1
        else:
            j -= 1
            i += 1
    return i