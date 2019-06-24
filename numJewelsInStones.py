def numJewelsInStones(self, J: str, S: str) -> int:
    result = {}
    for j in J:
        result[j] = 1
    res = 0
    for s in S:
        res += result.get(s, 0)
    return res

def numJewelsInStones(self, J: str, S: str) -> int:
    result = 0
    for s in S:
        if s in J:
            result += 1
    return result
    