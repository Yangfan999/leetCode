def lengthOfLongestSubstring(self, s):
    """
    :type s: str
    :rtype: int
    """
    r = ""
    k = [0]
    for string in s:
        if string not in r:
            r += string
        else:
            k.append(len(r))
            r = r[r.find(string) + 1:] + string
    k.append(len(r))
    return max(k)