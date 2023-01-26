#Without Comprehension
class Solution:
    def maximumWealth(self, accounts: List[List[int]]) -> int:
        y = []
        for account in accounts:
            x = sum(account)
            y.append(x)
        return (max(y))
      
      
#With Comprehensioon
class Solution:
    def maximumWealth(self, accounts: List[List[int]]) -> int:
        return max([(sum(account)) for account in accounts])
