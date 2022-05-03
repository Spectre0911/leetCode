class Solution(object):
    def removeElement(self, nums, val):
        """python
        :type nums: List[int]
        :type val: int
        :rtype: int
        """
        i, N = 0, len(nums)
        while i < N:
            if nums[i] != val:
                i += 1
            else:
                nums.pop(i)
            N = len(nums)
        return len(nums)