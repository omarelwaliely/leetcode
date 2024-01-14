class Solution(object):
    def hasCycle(self, head):
        fast,slow = head,head
        if not head:
            return False
        while(fast and fast.next):
            fast = fast.next.next
            slow = slow.next
            if fast == slow:
                return True
        return False