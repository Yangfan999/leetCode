def plusOne(self, digits: List[int]) -> List[int]:
    t = digits[-1]
    if t == 9:
        if len(digits) == 1:
            return [1,0]
        else:
            x = self.plusOne(digits[:-1]) + [0]
    else:
        x = digits[:-1] + [digits[-1] + 1]
    return x