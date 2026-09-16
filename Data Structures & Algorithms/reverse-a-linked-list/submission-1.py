# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head==None:
            print("Empty,irreversible!")
            return head
        curr=head
        arr=[]
        arr.append(curr)
        while curr.next is not None:
            curr=curr.next
            arr.append(curr)
        for i in range(len(arr)-1,0,-1):
            arr[i].next=arr[i-1]
        arr[0].next=None

        return arr[len(arr)-1]

