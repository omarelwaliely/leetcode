class Solution(object): #solution 1 (iterative)
    def reverseList(self, head):
        prev, curr = None,head
        while(curr):
            nxt = curr.next
            curr.next = prev
            prev = curr
            curr = nxt
        return prev #because head is null so it is not inside the linked list

    
class Solution(object): #solution 2 (recursive)
    def reverseList(self, head):
        def reverse(curr,prev):
            if not curr:
                return prev
            else:
                nxt = curr.next
                curr.next = prev
                return reverse(nxt,curr)
        return reverse(head,None)
        