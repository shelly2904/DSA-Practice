# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
from typing import Optional

from linkedlist import *


class Solution():
    def length(self, lst: Optional[Node]) -> int:
        if lst is None:
            return 0
        return 1 + self.length(lst.next)

    def add_two_number(self, ll_1: Optional[Node], ll_2: Optional[Node]) -> Optional[Node]:
        m = self.length(ll_1)
        n = self.length(ll_2)
        if m >= n:
            carryover = 0
            while ll_2 is not None:
                sum_val = ll_1.data + ll_2.data + carryover
                carryover = sum_val // 10
                sum_val = sum_val % 10
                ll_1.val = sum_val
                ll_2 = ll_2.next
                ll_1 = ll_1.next
            while ll_1 is not None:
                sum_val = ll_1.data + carryover
                carryover = sum_val // 10
                sum_val = sum_val % 10
                ll_1.val = sum_val
                ll_1 = ll_1.next
            print(ll_1)
        else:
            carryover = 0
            while ll_1 is not None:
                sum_val = ll_1.data + ll_2.data + carryover
                carryover = sum_val // 10
                sum_val = sum_val % 10
                ll_2.val = sum_val
                ll_1 = ll_2.next
                ll_1 = ll_1.next
            while ll_2 is not None:
                sum_val = ll_2.val + carryover
                carryover = sum_val // 10
                sum_val = sum_val % 10
                ll_2.val = sum_val
                ll_2 = ll_2.next
            print(ll_2)


if __name__ == "__main__":
    l1 = [2, 7, 3]
    l2 = [7, 9, 4]

    ll1 = LinkedList()
    for l in l1:
        node = Node(l)
        ll1.insert_at_end(node)

    ll2 = LinkedList()
    for l in l2:
        node = Node(l)
        ll2.insert_at_end(node)

    sol = Solution()
    sol.add_two_number(ll1, ll2)




