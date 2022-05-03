class Solution(object):
    def divideArray(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        
        frequency = {}
        
        for number in nums:
            currentFreq = frequency.get(number)
            if (currentFreq == None):
                frequency[number] = 1
            else:
                frequency[number] = currentFreq + 1
        
        for value in frequency.values():
            if (value % 2 != 0):
                return False
        return True