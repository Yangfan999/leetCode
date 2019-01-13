def letterCombinations(self, digits):
    """
    :type digits: str
    :rtype: List[str]
    """
    letter = {"2":["a","b","c"], "3":["d","e","f"], "4":["g","h","i"], "5":["j","k","l"],  "6":["m","n","o"],  "7":["p","q","r","s"],  "8":["t","u","v"],  "9":["w","x","y","z"]}
    result = []
    append = result.append
    if len(digits) == 0:
        return []
    if len(digits) == 1:
        return letter[digits]
    prev = self.letterCombinations(digits[:-1])
    additional = letter[digits[-1]]
    return [s + c for s in prev for c in additional]