class Solution(object):
    def reformatNumber(self, number):
        """
        :type number: str
        :rtype: str
        """
        formattedNumber = ""
        string = ""
        
        for i in range(len(number)):
            try:
                int(number[i:i+1])
                formattedNumber += number[i:i+1]
                
            except:
                continue
                
        
        i = 0
        while i < len(formattedNumber):
            
            if len(formattedNumber) - i == 4:
                string += formattedNumber[i:i+2]
                string += "-"
                string += formattedNumber[i+2:i+4]
                i+=4
            
            if len(formattedNumber) - i >= 3:
                string += formattedNumber[i:i+3]
                if len(formattedNumber) - i > 3:
                    string += "-"
                i+=3
            
            if len(formattedNumber) - i == 2:
                string += formattedNumber[i:i+2]
                i+=2
                
        return(string)