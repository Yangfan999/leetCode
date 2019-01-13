def longestCommonPrefix(self, strs):
    """
    :type strs: List[str]
    :rtype: str
    """
    if not len(strs):
        return ""
    i = min([len(s) for s in strs], default=0)
    j = 0
    while j != i:
        stra = strs[0][j]
        for s in strs:
            if s[j] != stra:
                return strs[0][0:j]
        j += 1
    return strs[0][0:j]