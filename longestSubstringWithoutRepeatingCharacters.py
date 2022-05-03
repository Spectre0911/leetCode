class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:              
        maximum = 0
        
        string = ""         
        head = 0     
        i = 0 
            
        while i+head < len(s):

            
            if s[i+head][0] not in string:
                string += s[i + head][0]
                i+=1
                
            else:
                head+=1
                string = ""
                i = 0
                          
            if i > maximum:
                maximum = i
                      
        
    
    
        return(maximum)