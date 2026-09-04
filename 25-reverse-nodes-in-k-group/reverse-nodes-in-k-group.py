
class Solution(object):
    def reverseKGroup(self, head, k):
        """
        :type head: Optional[ListNode]
        :type k: int
        :rtype: Optional[ListNode]
        """
        def get_kth(curr, k):
            while curr and k > 0:
                curr = curr.next
                k -= 1
            return curr

        dummy = ListNode(0, head)
        group_prev = dummy

        while True:
            # Check if there are at least k nodes left to reverse
            kth = get_kth(group_prev, k)
            if not kth:
                break
            
            group_next = kth.next

            # Reverse the k nodes
            prev, curr = kth.next, group_prev.next
            while curr != group_next:
                temp_next = curr.next
                curr.next = prev
                prev = curr
                curr = temp_next

            # Connect the reversed group with the rest of the list
            tmp = group_prev.next
            group_prev.next = kth
            group_prev = tmp

        return dummy.next