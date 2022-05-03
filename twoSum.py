class Solution(object):
    def twoSum(self, nums, target):
        
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        indexRoot = 0
        while indexRoot < len(nums):
                indexCompare = indexRoot + 1
                while indexCompare < len(nums):
                        if  nums[indexCompare] + nums[indexRoot] == target:
                               return(indexRoot,indexCompare)
                        indexCompare += 1
                indexRoot += 1