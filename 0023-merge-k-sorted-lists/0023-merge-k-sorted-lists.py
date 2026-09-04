import heapq

# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution(object):
    def mergeKLists(self, lists):
        """
        :type lists: List[Optional[ListNode]]
        :rtype: Optional[ListNode]
        """
        heap = []
        
        # Push the first node of each non-empty list into the heap.
        # We store a tuple of (node.val, index, node) to avoid comparison errors 
        # in Python when two nodes happen to have the same value.
        for i, l in enumerate(lists):
            if l:
                heapq.heappush(heap, (l.val, i, l))
                
        dummy = ListNode(0)
        curr = dummy
        
        while heap:
            val, i, node = heapq.heappop(heap)
            curr.next = node
            curr = curr.next
            
            # If there is a next node in the same linked list, push it to the heap
            if node.next:
                heapq.heappush(heap, (node.next.val, i, node.next))
                
        return dummy.next