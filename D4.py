class ListNode:
    def _init_(self, val=0, next=None):
        self.val = val
        self.next = next

def mergeTwoLists(l1, l2):
    
    dummy = ListNode(-1)
    current = dummy
    
   
    while l1 and l2:
       
        if l1.val <= l2.val:
            current.next = l1
            l1 = l1.next
        else:
            current.next = l2
            l2 = l2.next
        current = current.next
    
   
    current.next = l1 if l1 else l2
    
   
    return dummy.next


list1 = ListNode(1, ListNode(3, ListNode(5)))
list2 = ListNode(2, ListNode(4, ListNode(6)))


merged_list = mergeTwoLists(list1, list2)

while merged_list:
    print(merged_list.val, end=" ")
    merged_list = merged_list.next
