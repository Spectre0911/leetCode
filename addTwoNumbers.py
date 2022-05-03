class Solution(object):
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        carry = 0
        answer = ListNode(-1,None)
        
        temp = answer

        valueOne = 0
        valueSecond = 0

        while l1 != None or l2 != None:

            if l1 == None and l2 != None:
                valueOne = 0
                valueSecond = l2.val

            elif l2 == None and l1 != None :
                valueOne = l1.val
                valueSecond = 0
            
            else:
                valueOne = l1.val
                valueSecond = l2.val

            summation =  valueOne + valueSecond  + carry
            if summation >= 10:
                summation -= 10
                carry = 1
            else:
                carry = 0 
    
            if temp.val == -1:
                temp.val = summation
                
            else:
                temp.next = ListNode(summation,None)
                temp = temp.next
                
      
      
            if l1 != None and l2 == None:
                l1 = l1.next
                
            elif l1 == None and l2 != None:
                l2 = l2.next
            
            else:
                l1 = l1.next
                l2 = l2.next
                  
            
                
        
        if carry > 0:
            while temp.next != None:
                temp = temp.next
            temp.next = ListNode(carry,None)
        
        return answer