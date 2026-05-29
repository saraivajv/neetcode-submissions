# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        if not head or not head.next:
            return False
        
        lento = head
        rapido = head.next
        while rapido and rapido.next:
            if lento == rapido:
                return True
            lento = lento.next
            rapido = rapido.next.next
        return False

        