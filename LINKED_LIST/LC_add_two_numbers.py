# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
from typing import Optional

# from linkedlist import *

class LinkedList:
    def __init__(self, head=None):
        self.head = head

    def insert_at_front(self, node):
        # add at the front
        node.next = self.head
        self.head = node

    def insert_at_end(self, node):
        if self.head is None:
            self.head = node
            return
        # add at the end
        cur = self.head
        while cur.next:
            cur = cur.next
        cur.next = node
        node.next = None

    def insert_at_pos(self, node, pos):
        if not self.head and pos == 0:
            self.head = node
            return
        cur = self.head
        position = 0
        while cur:
            if position == pos:
                node.next = cur.next
                cur.next = node
                break
            else:
                position += 1
                cur = cur.next

    def delete_key(self, key):
        if self.head is None:
            return "Linked List empty"
        cur = self.head
        prev = None
        while cur:
            # print cur.data, prev.data
            if cur.val == key:
                if cur == self.head:
                    self.head = self.head.next
                    cur.next = None
                else:
                    prev.next = cur.next
                    cur.next = None
                return True
            prev = cur
            cur = cur.next
        return "Key doesnot exists"

    def delete_at_pos(self, pos):
        if self.head is None:
            return "Linked List empty"
        cur = self.head
        prev = None
        position = 0
        while cur:
            # print cur.data, prev.data
            if position == pos:
                if cur == self.head:
                    self.head = self.head.next
                    cur.next = None
                else:
                    prev.next = cur.next
                    cur.next = None
                return True
            prev = cur
            cur = cur.next
            position += 1
        return "Key doesnot exists"

    def traversal(self):
        current = self.head
        while current:
            print(current.val)
            current = current.next



class Solution():
    def add_two_number(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> LinkedList:

        # For returning the head
        # def addTwoNumbers(self, l1, l2):
        #     """
        #     :type l1: ListNode
        #     :type l2: ListNode
        #     :rtype: ListNode
        #     """
        #     dummy_head = ListNode(0)
        #     l3 = dummy_head
        #     carry = 0
        #
        #     while l1 or l2:
        #         l1_val = l1.val if l1 else 0
        #         l2_val = l2.val if l2 else 0
        #
        #         sum_ = l1_val + l2_val + carry
        #         carry = sum_ // 10
        #         sum_ = sum_ % 10
        #
        #         dummy_node = ListNode(sum_)
        #         l3.next = dummy_node
        #
        #         l1 = l1.next if l1 else None
        #         l2 = l2.next if l2 else None
        #         l3 = l3.next
        #
        #     if carry > 0:
        #         dummy_node = ListNode(carry)
        #         l3.next = dummy_node
        #         l3 = l3.next
        #
        #     return dummy_head.next

        l3 = LinkedList()
        carry = 0

        while l1 or l2:
            l1_val = l1.val if l1 else 0
            l2_val = l2.val if l2 else 0

            sum_ = l1_val + l2_val + carry
            carry = sum_ // 10
            sum_ = sum_ % 10

            l3.insert_at_end(ListNode(sum_))

            l1 = l1.next if l1 else None
            l2 = l2.next if l2 else None

        if carry > 0:
            l3.insert_at_end(ListNode(carry))

        return l3


# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution2(object):
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """

        global dummy_head
        stack1 = []
        stack2 = []

        l1_head = l1
        l2_head = l2

        while l1_head:
            stack1.append(l1_head.val)
            l1_head = l1_head.next

        while l2_head:
            stack2.append(l2_head.val)
            l2_head = l2_head.next


        start = 0

        carry = 0
        while stack1 or stack2:
            l1_val = stack1.pop() if stack1 else 0
            l2_val = stack2.pop() if stack2 else 0

            sum_val = l1_val + l2_val + carry
            carry = sum_val // 10
            sum_val = sum_val % 10

            if start == 0:
                dummy_head = ListNode(sum_val)
            else:
                dummy_node = ListNode(sum_val)
                dummy_node.next = dummy_head
                dummy_head = dummy_node
            start += 1

        if carry > 0:
            dummy_node = ListNode(carry)
            dummy_node.next = dummy_head
            dummy_head = dummy_node

        return dummy_head

def traversal(head):
    current = head
    while current:
        print(current.val)
        current = current.next

if __name__ == "__main__":
    l1 = [5]
    l2 = [5]

    ll_1 = LinkedList()
    for l in l1:
        node = ListNode(l)
        ll_1.insert_at_end(node)

    ll_2 = LinkedList()
    for l in l2:
        node = ListNode(l)
        ll_2.insert_at_end(node)

    sol = Solution2()

    result = sol.addTwoNumbers(ll_1.head, ll_2.head)
    traversal(result)


