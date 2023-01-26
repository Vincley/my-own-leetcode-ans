#Two pointer
class Solution:

    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
        x = y = head

        while x and x.next:
            x = x.next.next
            y = y.next
        return y
      
#While loop
class Solution:

    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
        count = 0
        current = head

        while current:
            count += 1
            current = current.next

        middle = count//2

        while middle:
            head = head.next
            middle -= 1
            
        return head
