class Solution:
    def maximumWealth(self, accounts: List[List[int]]) -> int:
        maximum = 0
        for j in range(0,len(accounts)):
            temp = 0      
            for i in range(0,len(accounts[j])):     
                temp += accounts[j][i]        
            if temp > maximum:
                maximum = temp
        return(maximum)