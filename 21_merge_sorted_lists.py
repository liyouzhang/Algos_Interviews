'''
Merge two sorted linked lists and return it as a new list. The new list should be made by splicing together the nodes of the first two lists.

Example:

Input: 1->2->4, 1->3->4
Output: 1->1->2->3->4->4
'''

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None



## 20200414 solution 1 - iteration 
class Solution:
    def mergeTwoLists(self, l1, l2):
        # maintain an unchanging reference to node ahead of the return node.
        prehead = ListNode(-1)

        prev = prehead
        while l1 and l2:
            if l1.val <= l2.val:
                prev.next = l1
                l1 = l1.next
            else:
                prev.next = l2
                l2 = l2.next            
            prev = prev.next

        # exactly one of l1 and l2 can be non-null at this point, so connect
        # the non-null list to the end of the merged list.
        prev.next = l1 if l1 is not None else l2

        return prehead.next

## 20200414 my thoughts
class Solution:
    def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
        # need to start with the tail because otherwise lose reference during the assignment
        # find the tail of the linked list for both l1 and l2 
        # and assign the l1.tail.next = l2.tail.next 



## 20200413 try - I don't understand linked list yet 
class Solution:
    def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
        # use a pointer index 
        # append the output list by index 
        output = []
        max_idx = max(len(l1),len(l2)) 
        for idx in range(max_idx):
            if idx < len(l1):
                output.append(l1[idx])
            if idx < len(l2):
                output.append(l2[idx])
        return output 