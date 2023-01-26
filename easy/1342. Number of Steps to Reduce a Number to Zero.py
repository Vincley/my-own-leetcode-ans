class Solution:
    def numberOfSteps(self, num: int) -> int:
        i = 0
        j = [num]
        for num in j:
            if num % 2 == 1:
                num -= 1
                i += 1
            if num == 0:
                i -= 1
                
        while num % 2 == 0:
            num /= 2
            i += 1
            if num % 2 == 1:
                num -= 1
                i += 1
            if num == 0:
                break
        return i
