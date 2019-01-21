    def generateParenthesis(self, n):
        """
        :type n: int
        :rtype: List[str]
        """
        if n == 1:
            return ["()"]
        result = set()
        for s in self.generateParenthesis(n-1):
            for i in range(len(s)):
                result.add(s[:i+1] + "()" + s[i+1:])
        return list(result)
        