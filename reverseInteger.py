class Solution(object):
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """
        y = str(x)


        if x>=0:
            counter = 0
            string = ""
        else:
            counter = 1
            string = "-"

        for i in range(len(y),0+counter,-1):
            string += y[i-1:i]
        
        number = int(string)

        if number > 2**31 or number < -2**31:
            number = 0
            
        return(number)