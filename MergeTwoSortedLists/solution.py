'''
Merge two sorted linked lists and return it as a sorted list. 
The list should be made by splicing together the nodes of the 
first two lists.
'''
from typing import List, Optional
from ListNode import ListNode

def print_linked_list(ll):
  output = []
  head = ll

  if head is None:
    return ''

  while head.next is not None:
    output.append(str(head.val))
    output.append(' -> ')

    head = head.next

  output.append(str(head.val))

  print(''.join(output))

class Solution:
  def mergeTwoLists(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
    solution = ListNode()
    curr_node = solution

    while l1 is not None and l2 is not None:
      if l1.val == l2.val:
        curr_node.next = ListNode(l1.val)
        curr_node = curr_node.next

        curr_node.next = ListNode(l2.val)
        curr_node = curr_node.next

        l1 = l1.next
        l2 = l2.next
      
      elif l1.val < l2.val:
        curr_node.next = ListNode(l1.val)
        curr_node = curr_node.next
        l1 = l1.next

      else:
        curr_node.next = ListNode(l2.val)
        curr_node = curr_node.next
        l2 = l2.next
    
    while l1 is not None:
        curr_node.next = ListNode(l1.val)
        curr_node = curr_node.next
        l1 = l1.next
  
    while l2 is not None:
        curr_node.next = ListNode(l2.val)
        curr_node = curr_node.next
        l2 = l2.next
    
    return solution.next
    

test_1 = ListNode(1)
test_1.next = ListNode(2)
test_1.next.next = ListNode(4)

test_2 = ListNode(1)
test_2.next = ListNode(3)
test_2.next.next = ListNode(4)

sol = Solution()

print_linked_list(sol.mergeTwoLists(test_1, test_2))