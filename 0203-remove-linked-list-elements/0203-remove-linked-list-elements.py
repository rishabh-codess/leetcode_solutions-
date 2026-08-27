# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeElements(self, head: Optional[ListNode],  val: int) -> Optional[ListNode]:

        while head is not None and head.val==val:
            head=head.next

        if head is None:
            return None
           

        temp =head

        while temp.next is not None:
            if  temp.next.val==val:
                nodetobedeleted=temp.next
                nodeafterdeleted=nodetobedeleted.next
                temp.next=nodeafterdeleted
        
            else:

                temp=temp.next
            

        return head

        