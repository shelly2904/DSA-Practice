from collections import deque


class Solution(object):
    def isPalindrome(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """
        stack = []

        p = head
        q = head

        while q and q.next:
            stack.append(p.val)
            p = p.next
            q = q.next.next

        if q:
            p = p.next

        while p:
            if stack.pop() != p.val:
                return False
            p = p.next

        return True