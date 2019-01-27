def removeDuplicates(self, nums):
    """
    :type nums: List[int]
    :rtype: int
    """
    if not nums:
        return 0
    l = len(nums)
    if l == 1:
        return 1
    cand = nums[0]
    i = 1
    while i < l:
        if cand == nums[i]:
            nums.pop(i)
            l -= 1
        else:
            cand = nums[i]
            i += 1
