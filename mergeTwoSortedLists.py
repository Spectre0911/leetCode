# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def mergeTwoLists(self, list1, list2):
        if not list1:
            return list2

        if not list2:
            return list1

        cur1, cur2, res = list1, list2, []

        while cur1:
            res.append(cur1.val)
            cur1 = cur1.next

        while cur2:
            res.append(cur2.val)
            cur2 = cur2.next

        res = sorted(res)

        ans = final_ans = ListNode()

        for i in range(len(res)):
            ans.next = ListNode(res[i])
            ans = ans.next

        return final_ans.next