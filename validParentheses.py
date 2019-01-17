    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        d = {"(":")", "{":"}", "[":"]"}
        match = []
        ma = match.append
        for i in s:
            if i in d.keys():
                ma(d[i])
            elif match and i == match[-1]:
                match.pop()
            else:
                return False
        return len(match) == 0