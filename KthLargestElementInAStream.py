class KthLargest(object):
    def __init__(self, gK, gNums):
        """
        :type k: int
        :type nums: List[int]
        """
        self.nums = gNums
        self.k = gK
        self.nums.sort()

    def add(self, val):
        """
        :type val: int
        :rtype: int
        """
        i = 0
        numLength = len(self.nums)
        while (i < numLength and self.nums[i] < val):
            i += 1
       