class Solution(object):
    def threeSum(self, lst):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        
        """
        n = len(lst)
        lst.sort()
        my_sol = set()
        for i in range(n-2):
            j = i+1
            k = n-1
            while j < k:
                current_sum = lst[i] + lst[j] + lst[k]
                if current_sum == 0:
                    my_sol.add((lst[i], lst[j], lst[k]))
                    j += 1
                    k -= 1
                elif current_sum < 0:
                    j += 1
                elif current_sum > 0:
                    k -= 1
        return [list(x) for x in my_sol]  